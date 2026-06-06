import joblib
import pandas as pd

from config import MODEL_PATH


def predict_churn():

    model = joblib.load(MODEL_PATH)

    sample_customer = {
        "gender": 0,
        "SeniorCitizen": 0,
        "Partner": 1,
        "Dependents": 0,
        "tenure": 1,
        "PhoneService": 1,
        "MultipleLines": 0,
        "InternetService": 1,
        "OnlineSecurity": 0,
        "OnlineBackup": 0,
        "DeviceProtection": 0,
        "TechSupport": 0,
        "StreamingTV": 0,
        "StreamingMovies": 0,
        "Contract": 0,
        "PaperlessBilling": 1,
        "PaymentMethod": 2,
        "MonthlyCharges": 95.5,
        "TotalCharges": 95.5
    }

    customer_df = pd.DataFrame(
        [sample_customer]
    )

    prediction = model.predict(
        customer_df
    )[0]

    if prediction == 1:
        print("Prediction: Customer likely to churn")
    else:
        print("Prediction: Customer likely to stay")


if __name__ == "__main__":
    predict_churn()