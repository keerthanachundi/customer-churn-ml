import joblib
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from src.config import (
    MODEL_PATH,
    APP_ENV,
    APP_VERSION
)

from fastapi import FastAPI
from src.schema import CustomerData
from src.response_schema import (
    PredictionResponse
)
from fastapi import HTTPException

app = FastAPI()

model = joblib.load(
    MODEL_PATH
)
logging.info(
    "Model loaded successfully"
)


@app.get("/")
def home():
    return {
        "message": "Customer Churn API Running"
    }
@app.get("/health")
def health():
    logging.info(
        "Health endpoint called"
    )


    return {
        "status": "healthy"
    }

@app.get("/info")
def info():

   
    return {
        "environment": APP_ENV,
        "version": APP_VERSION
       
    }



@app.post(
    "/api/v1/predict",
    response_model=PredictionResponse
)
def predict(customer: CustomerData):
    logging.info(
    "Prediction request received"
)

    customer_df = pd.DataFrame(
        [customer.model_dump()]
    )

    try:

        prediction = model.predict(
            customer_df
        )[0]

    except Exception as e:
        logging.error(
    f"Prediction failed: {str(e)}"
)

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

    logging.info(
    f"Prediction result: {result}"
)

    return PredictionResponse(
        prediction=result
    )