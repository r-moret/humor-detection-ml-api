import os
import pathlib
import argparse

import kaggle
import pandas as pd
from sklearn.model_selection import train_test_split

DEFAULT_SPLIT_SEED = 42


def obtain_data(directory: str, *, split_seed: int = DEFAULT_SPLIT_SEED) -> None:
    KAGGLE_DATASET_LOCATION = "deepcontractor/200k-short-texts-for-humor-detection"
    KAGGLE_DATASET_NAME = "dataset.csv"

    data_folder = pathlib.Path(directory)

    api = kaggle.KaggleApi()
    api.authenticate()

    print(f'Downloading "{KAGGLE_DATASET_NAME}" from {KAGGLE_DATASET_LOCATION} ...')
    api.dataset_download_files(
        dataset=KAGGLE_DATASET_LOCATION, path=data_folder, unzip=True
    )
    print("Download succesful!")

    dataset = pd.read_csv(data_folder / KAGGLE_DATASET_NAME)
    train, test = train_test_split(dataset, test_size=0.2, random_state=split_seed)

    train.to_csv(data_folder / "train.csv", index=False)
    test.to_csv(data_folder / "test.csv", index=False)
    os.remove(data_folder / KAGGLE_DATASET_NAME)

    print(f'\nSplitted "{KAGGLE_DATASET_NAME}" on "{data_folder}"')
    print(f"TRAIN: {len(train)}")
    print(f"TEST:  {len(test)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--obtain_data",
        help="indicates that the functionality of the execution is obtaining the training data. Must contains the path to the directory where you want to save the data obtained",
    )
    parser.add_argument(
        "--split_seed",
        default=DEFAULT_SPLIT_SEED,
        type=int,
        help="random seed to use when splitting the data in train/test. Only can be used when `obtain_data` is used",
    )

    arguments = vars(parser.parse_args())

    if arguments["obtain_data"]:
        obtain_data(arguments["obtain_data"], split_seed=arguments["split_seed"])
