import os
from dotenv import load_dotenv

load_dotenv()

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