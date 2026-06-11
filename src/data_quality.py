import pandas as pd


def validate_orders_data(df: pd.DataFrame) -> None:
    """Validate cleaned orders data before loading."""

    required_columns = [
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp",
    ]

    # Check required columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Check missing order_id
    if df["order_id"].isna().any():
        raise ValueError("order_id contains missing values.")

    # Check duplicated order_id
    if df["order_id"].duplicated().any():
        raise ValueError("order_id contains duplicated values.")

    # Check missing customer_id
    if df["customer_id"].isna().any():
        raise ValueError("customer_id contains missing values.")

    # Check invalid purchase timestamp
    invalid_dates = pd.to_datetime(
        df["order_purchase_timestamp"],
        errors="coerce"
    ).isna()

    if invalid_dates.any():
        raise ValueError("order_purchase_timestamp contains invalid dates.")

    print("Data quality check passed.")