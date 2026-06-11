import pandas as pd


def extract_data(file_path: str) -> pd.DataFrame:
    """Load raw ecommerce sales data from CSV."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {file_path}") from exc