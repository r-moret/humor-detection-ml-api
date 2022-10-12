import json
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import pandas as pd
import tensorflow as tf
from huggingface_hub import HfApi
from pydantic import BaseModel
from sklearn.metrics import accuracy_score, f1_score
from transformers import BertTokenizer, TFBertForSequenceClassification

TextCorpus = Union[List[str], pd.Series]
LabelsSequence = Union[List[int], List[bool], pd.Series]
MetricFunction = Callable[[LabelsSequence, LabelsSequence], float]


class HumorModel(BaseModel):
    bert: TFBertForSequenceClassification
    tokenizer: BertTokenizer
    metrics: Optional[Dict]

    def __init__(self, model_name: str, **data: Any) -> None:
        super().__init__(
            bert=TFBertForSequenceClassification.from_pretrained(model_name),
            tokenizer=BertTokenizer.from_pretrained(model_name),
            **data,
        )

    def predict(self, sentences: TextCorpus) -> List[Tuple[int, float]]:
        processed_sentences = self._preprocess(sentences)

        logits = self.bert.predict(processed_sentences).logits
        classes_probability = tf.nn.softmax(logits, axis=1)

        predicted_label = tf.argmax(classes_probability, axis=1).numpy()
        predicted_probability = tf.reduce_max(classes_probability, axis=1).numpy()

        preds_w_probability = list(zip(predicted_label, predicted_probability))
        return preds_w_probability

    def train(
        self,
        train_set: Tuple[TextCorpus, LabelsSequence],
        *,
        test_set: Optional[Tuple[TextCorpus, LabelsSequence]] = None,
        optimizer: tf.keras.optimizers.Optimizer = tf.keras.optimizers.Adam(3e-5),
        **eval_kwargs,
    ) -> Optional[Dict]:
        sentences, labels = train_set
        processed_sentences = self._preprocess(sentences)

        self.bert.compile(optimizer=optimizer)
        self.bert.fit(processed_sentences, labels)

        if test_set:
            self.metrics = self.evaluate(*test_set, **eval_kwargs)
            return self.metrics

    def evaluate(
        self,
        sentences: TextCorpus,
        labels: LabelsSequence,
        *,
        metrics: List[MetricFunction] = [accuracy_score, f1_score],  # type: ignore
    ) -> Dict:
        processed_sentences = self._preprocess(sentences)

        logits = self.bert.predict(processed_sentences).logits
        classes_probability = tf.nn.softmax(logits, axis=1)
        predicted_labels = tf.argmax(classes_probability, axis=1).numpy()

        results = {
            metric.__name__: metric(labels, predicted_labels) for metric in metrics
        }

        return results

    def _preprocess(self, sentences: TextCorpus) -> Dict:
        if isinstance(sentences, pd.Series):
            sentences = sentences.to_list()

        tokenized_sentences = self.tokenizer(
            sentences, return_tensors="tf", truncation=True, padding=True
        )

        return tokenized_sentences.data

    def push_to_hub(self, repo_id: str) -> None:
        _, model_name = repo_id.split("/")

        self.bert.push_to_hub(model_name)
        self.tokenizer.push_to_hub(model_name)

        if self.metrics:
            bytes_metrics = json.dumps(self.metrics).encode("utf-8")
        else:
            bytes_metrics = json.dumps({"State": "Model not evaluated"}).encode("utf-8")

        api = HfApi()
        api.upload_file(
            path_or_fileobj=bytes_metrics,
            path_in_repo="metrics.json",
            repo_id=repo_id,
            repo_type="model",
        )

    class Config:
        arbitrary_types_allowed = True
