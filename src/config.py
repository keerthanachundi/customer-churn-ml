import os
from dotenv import load_dotenv

load_dotenv()

RAW_DATA_PATH = os.getenv(
    "RAW_DATA_PATH",
    "data/raw/customer_churn.csv"
)

PROCESSED_DATA_PATH = os.getenv(
    "PROCESSED_DATA_PATH",
    "data/processed/processed_customer_churn.csv"
)

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "models/churn_model.pkl"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "v1"
)