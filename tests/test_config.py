from src.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    MODEL_PATH
)


def test_raw_data_path():

    assert RAW_DATA_PATH == \
        "data/raw/customer_churn.csv"


def test_processed_data_path():

    assert PROCESSED_DATA_PATH == \
        "data/processed/processed_customer_churn.csv"


def test_model_path():

    assert MODEL_PATH == \
        "models/churn_model.pkl"