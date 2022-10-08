import os
import pathlib

import kaggle
import pandas as pd
from sklearn.model_selection import train_test_split

KAGGLE_DATASET_LOCATION = "deepcontractor/200k-short-texts-for-humor-detection"
KAGGLE_DATASET_NAME = "dataset.csv"
DATA_FOLDER = pathlib.Path("./machine-learning/data")
SPLIT_SEED = 42

api = kaggle.KaggleApi()
api.authenticate()

print(f'Downloading "{KAGGLE_DATASET_NAME}" from {KAGGLE_DATASET_LOCATION} ...')
api.dataset_download_files(
    dataset=KAGGLE_DATASET_LOCATION, path=DATA_FOLDER, unzip=True
)
print("Download succesful!")

dataset = pd.read_csv(DATA_FOLDER / KAGGLE_DATASET_NAME)
train, test = train_test_split(dataset, test_size=0.2, random_state=SPLIT_SEED)

train.to_csv(DATA_FOLDER / "train.csv")
test.to_csv(DATA_FOLDER / "test.csv")
os.remove(DATA_FOLDER / KAGGLE_DATASET_NAME)

print(f'\nSplitted "{KAGGLE_DATASET_NAME}" on "{DATA_FOLDER}"')
print(f"TRAIN: {len(train)}")
print(f"TEST:  {len(test)}")
