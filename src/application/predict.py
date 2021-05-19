"""
    This module is one of the two entrypoints with train.py
    It is used to make predictions using our model.
"""

import pickle
import logging
from typing import Union
from warnings import simplefilter
import os
import glob
from click.exceptions import FileError

import pandas as pd
from pandas.core.common import SettingWithCopyWarning
import click

import src.config.base as base
import src.config.column_names as col
from src.domain.cleaning import correct_wrong_entries, impute_missing_eco_data
from src.infrastructure.build_dataset import DataBuilderFactory, DataMerger
from src.infrastructure.utils import download_blob

# Ignorer les warnings pour améliorer la lisibilité
simplefilter(action="ignore", category=FutureWarning)
simplefilter(action="ignore", category=SettingWithCopyWarning)


def load_pipeline():
    """Loads model from pickle file."""

    try:
        logging.info("Loading the fitted pipeline...")
        with open(base.SAVED_MODEL_PATH, "rb") as model_file:
            pipeline = pickle.load(model_file)
        logging.info("Loading completed successfully...")
    except FileNotFoundError:
        logging.error("Model file has not been found.")
        raise
    return pipeline


# @click.command(help="Make a prediction about whether will subscribe or not")
def main(prediction_data_path=base.PREDICT_CLIENT_DATA_PATH, run_type: str = "normal"):

    # Builds datasets.
    logging.info("Building datasets...")
    client_builder = DataBuilderFactory(
        prediction_data_path, base.config_client_data, base.ALL_CLIENT_DATA_TRANSLATION
    )
    client_data = client_builder.preprocess_data().data

    eco_builder = DataBuilderFactory(base.PREDICT_ECO_DATA_PATH, base.config_eco_data)
    eco_data = eco_builder.preprocess_data().data

    logging.info("Preprocessing...")
    # Imputes NaN from the eco dataset.
    # This step is done outside the pipeline to avoid duplication of NaN while merging.
    eco_data = impute_missing_eco_data(eco_data)
    # Fixes erroneous entries in client dataset.
    client_data = correct_wrong_entries(
        client_data, base.config_client_data.get("wrong_entries")
    )

    # Merges client and eco datasets.
    logging.info("Merging client and eco datasets...")
    merged = DataMerger(client_data, eco_data, col.MERGER_FIELD)
    merged.merge_datasets()
    X_pred = merged.joined_datasets
    if col.TARGET in X_pred.columns:
        X_pred.drop(col.TARGET, axis=1, inplace=True)

    # Loads pipeline.
    pipeline = load_pipeline()

    # Makes predictions.
    X_pred.dropna(axis=0)
    y_pred = pipeline.predict(X_pred)
    # Writes predictions.
    if run_type == "normal":
        y_pred = pd.Series(y_pred)
        y_pred.to_csv(base.PREDICTIONS_FILE_PATH)
    elif run_type == "api":
        if y_pred[0] == 0:
            return "N'a pas souscrit"
        elif y_pred[0] == 1:
            return "A souscrit"


if __name__ == "__main__":
    main()
