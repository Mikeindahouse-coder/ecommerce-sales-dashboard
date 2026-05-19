import sqlite3
from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")
DB_PATH = Path("olist_ecommerce.db")

csv_to_table = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "payments",
    "olist_order_reviews_dataset.csv": "reviews",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "olist_geolocation_dataset.csv": "geolocation",
    "product_category_name_translation.csv": "product_category_translation",
}


def main() -> None:
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data folder not found: {DATA_DIR.resolve()}")

    with sqlite3.connect(DB_PATH) as conn:
        for csv_file, table_name in csv_to_table.items():
            csv_path = DATA_DIR / csv_file

            if not csv_path.exists():
                print(f"Skipped missing file: {csv_path}")
                continue

            print(f"Loading {csv_file} -> {table_name}")

            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)

            print(f"Loaded {len(df):,} rows into {table_name}")

    print(f"\nDone. SQLite database created: {DB_PATH.resolve()}")


if __name__ == "__main__":
    main()