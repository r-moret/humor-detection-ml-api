import argparse
from typing import Optional, Tuple

import pandas as pd

from humor import HumorModel

# TODO: Add posibility to train with GPU
# TODO: Eliminate all the verbose messages from the CLI execution
# TODO: Add model evaluation on test_data and upload the metrics to the Hub
# TODO: Explore the possibility to unify utils.py and train.py in one single main.py

def train(
    model_name: str,
    train_data: Tuple[pd.Series, pd.Series],
    *,
    test_data: Optional[Tuple[pd.Series, pd.Series]] = None,
    upload_to_hub: bool = False,
) -> None:
    model = HumorModel("bert-base-uncased")

    train_texts, train_labels = train_data
    model.train(train_texts, train_labels)

    if upload_to_hub:
        model.push_to_hub(model_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model_name", required=True, help="name with which the model will be saved"
    )
    parser.add_argument(
        "--train_data",
        required=True,
        help=(
            "path to the training data. It must be a CSV file with two columns, one "
            "named `text` for the sentences and another named `humor` for the labels"
        ),
    )
    parser.add_argument(
        "--test_data",
        help=(
            "path to the test data. It must be a CSV file with two columns, one "
            "named `text` for the sentences and another named `humor` for the labels"
        ),
    )
    parser.add_argument(
        "--upload_to_hub",
        action="store_true",
        default=False,
        help="indicates if after the training the model has to be uploaded into the Huggingface Hub",
    )

    arguments = vars(parser.parse_args())

    train_data = pd.read_csv(arguments["train_data"])

    if arguments["test_data"]:
        test_data = pd.read_csv(arguments["test_data"])
        train(
            arguments["model_name"],
            (train_data["text"], train_data["humor"]),
            test_data=(test_data["text"], test_data["humor"]),
            upload_to_hub=arguments["upload_to_hub"],
        )
    else:
        train(
            arguments["model_name"],
            (train_data["text"], train_data["humor"]),
            upload_to_hub=arguments["upload_to_hub"],
        )
