import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform ecommerce sales data."""
    df = df.copy()

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Drop rows with missing order id if the column exists
    if "order_id" in df.columns:
        df = df.dropna(subset=["order_id"])

    # Convert date column if available
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Create revenue column if quantity and price exist
    if {"quantity", "price"}.issubset(df.columns):
        df["revenue"] = df["quantity"] * df["price"]

    return df