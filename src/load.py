import sqlite3
import pandas as pd


def load_data(df: pd.DataFrame, output_path: str) -> None:
    """Save transformed data to CSV."""
    df.to_csv(output_path, index=False)


def load_data_to_sqlite(
    df: pd.DataFrame,
    db_path: str,
    table_name: str
) -> None:
    """Load transformed data into a SQLite table."""
    conn = sqlite3.connect(db_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()