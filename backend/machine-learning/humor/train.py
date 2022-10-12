import argparse
from typing import Optional, Tuple

import pandas as pd

from humor import HumorModel

# TODO: Add posibility to train with GPU
# TODO: Eliminate all the verbose messages from the CLI execution
# TODO: Explore the possibility to unify utils.py and train.py in one single main.py
# TODO: Make some metrics functions available to use when executed through CLI
# TODO: Fix long import time of humor lib


def train(
    train_data: Tuple[pd.Series, pd.Series],
    repo_id: Optional[str] = None,
    *,
    test_data: Optional[Tuple[pd.Series, pd.Series]] = None,
) -> None:
    model = HumorModel("bert-base-uncased")

    model.train(train_data, test_set=test_data)

    if repo_id:
        model.push_to_hub(repo_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

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
        "--push_to_hub",
        help=(
            "indicates if after training the model has to be uploaded into the "
            "HuggingFace Hub. Its value is the repository id where the model will be "
            'saved, in the form of "username/repository_name"'
        ),
    )

    arguments = vars(parser.parse_args())

    train_data = pd.read_csv(arguments["train_data"])

    test_data = None
    if arguments["test_data"]:
        test_data = pd.read_csv(arguments["test_data"])
        test_data = (test_data["text"], test_data["humor"])

    train(
        (train_data["text"], train_data["humor"]),
        repo_id=arguments["push_to_hub"],
        test_data=test_data,
    )
