import joblib
import pandas as pd

from fastapi import FastAPI
from src.schema import CustomerData
from src.config import MODEL_PATH
from src.response_schema import (
    PredictionResponse
)
from fastapi import HTTPException

app = FastAPI()

model = joblib.load(
    MODEL_PATH
)


@app.get("/")
def home():
    return {
        "message": "Customer Churn API Running"
    }
@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post(
    "/api/v1/predict",
    response_model=PredictionResponse
)
def predict(customer: CustomerData):

    customer_df = pd.DataFrame(
        [customer.model_dump()]
    )

    try:

        prediction = model.predict(
            customer_df
        )[0]

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    if prediction == 1:

        result = (
            "Customer likely to churn"
        )

    else:

        result = (
            "Customer likely to stay"
        )

    return PredictionResponse(
        prediction=result
    )