import pandas as pd
from sklearn.preprocessing import LabelEncoder

from config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    TARGET_COLUMN
)


def preprocess_data():

    print("Loading dataset...")

    df = pd.read_csv(RAW_DATA_PATH)

    print(f"Dataset shape: {df.shape}")

    # Remove customerID
    if "customerID" in df.columns:
        df.drop(columns=["customerID"], inplace=True)

    # Handle TotalCharges
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Fill missing values
    df.fillna(0, inplace=True)

    # Encode categorical columns
    label_encoder = LabelEncoder()

    for column in df.columns:

        if df[column].dtype in ["object", "string"] or str(df[column].dtype) in ["object", "string", "str"]:

            print(f"Encoding column: {column}")

            df[column] = LabelEncoder().fit_transform(
                df[column].astype(str)
            )

      

            

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print(
        f"Processed dataset saved to: "
        f"{PROCESSED_DATA_PATH}"
    )

    print("Preprocessing completed successfully")


if __name__ == "__main__":
    preprocess_data()