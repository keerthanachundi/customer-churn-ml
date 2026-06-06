import os
import pandas as pd


DATASET_PATH = "data/raw/customer_churn.csv"

REQUIRED_COLUMNS = [
    "customerID",
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "InternetService",
    "Contract",
    "MonthlyCharges",
    "TotalCharges",
    "Churn"
]


def validate_file_exists(file_path):
    """
    Check whether dataset exists.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    print("SUCCESS: Dataset file exists")


def validate_dataset_not_empty(df):
    """
    Check dataset contains records.
    """

    if df.empty:
        raise ValueError(
            "Dataset is empty"
        )

    print("SUCCESS: Dataset contains data")


def validate_required_columns(df):
    """
    Check required columns exist.
    """

    missing_columns = []

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    print("SUCCESS: Required columns found")


def validate_target_column(df):
    """
    Check target column exists.
    """

    if "Churn" not in df.columns:
        raise ValueError(
            "Target column Churn not found"
        )

    print("SUCCESS: Target column exists")


def validate_duplicate_customers(df):
    """
    Check duplicate customer IDs.
    """

    duplicate_count = df["customerID"].duplicated().sum()

    if duplicate_count > 0:
        print(
            f"WARNING: {duplicate_count} duplicate customer IDs found"
        )
    else:
        print(
            "SUCCESS: No duplicate customer IDs"
        )


def run_validation():

    validate_file_exists(DATASET_PATH)

    df = pd.read_csv(DATASET_PATH)

    validate_dataset_not_empty(df)

    validate_required_columns(df)

    validate_target_column(df)

    validate_duplicate_customers(df)

    print("\nDATA VALIDATION COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    run_validation()