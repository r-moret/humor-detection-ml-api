from typing import Any, Dict, List, Tuple, Union

import pandas as pd
import tensorflow as tf
from pydantic import BaseModel
from transformers import BertTokenizer, TFBertForSequenceClassification


class HumorModel(BaseModel):
    bert: TFBertForSequenceClassification
    tokenizer: BertTokenizer

    def __init__(self, model_name: str, **data: Any) -> None:
        super().__init__(
            bert=TFBertForSequenceClassification.from_pretrained(model_name),
            tokenizer=BertTokenizer.from_pretrained(model_name),
            **data
        )

    def predict(
        self, sentences: Union[List[str], pd.Series]
    ) -> List[Tuple[int, float]]:
        if isinstance(sentences, pd.Series):
            sentences = sentences.to_list()

        processed_sentences = self._preprocess(sentences)

        logits = self.bert.predict(processed_sentences).logits
        classes_probability = tf.nn.softmax(logits, axis=1)

        predicted_label = tf.argmax(classes_probability, axis=1).numpy()
        predicted_probability = tf.reduce_max(classes_probability, axis=1).numpy()

        preds_w_probability = list(zip(predicted_label, predicted_probability))
        return preds_w_probability

    def train(
        self,
        sentences: Union[List[str], pd.Series],
        labels: Union[List[int], List[bool], pd.Series],
        *,
        optimizer: tf.keras.optimizers.Optimizer = tf.keras.optimizers.Adam(3e-5)
    ) -> None:
        if isinstance(sentences, pd.Series):
            sentences = sentences.to_list()

        processed_sentences = self._preprocess(sentences)

        self.bert.compile(optimizer=optimizer)
        self.bert.fit(processed_sentences, labels)

    def _preprocess(self, sentences: List[str]) -> Dict:
        tokenized_sentences = self.tokenizer(
            sentences, return_tensors="tf", truncation=True, padding=True
        )

        return tokenized_sentences.data

    class Config:
        arbitrary_types_allowed = True
