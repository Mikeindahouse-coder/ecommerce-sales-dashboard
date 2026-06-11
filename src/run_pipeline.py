import logging
import os

from build_analytics import build_analytics_table
from extract import extract_data
from transform import transform_data
from load import load_data_to_sqlite


DATA_MODE = os.getenv("DATA_MODE", "raw")

if DATA_MODE == "sample":
    DATA_DIR = "data/sample"
    FILE_SUFFIX = "sample"
else:
    DATA_DIR = "data/raw"
    FILE_SUFFIX = "dataset"


DB_PATH = "olist_ecommerce.db"
ANALYTICS_SQL_PATH = "sql/10_create_analytics_sales.sql"


TABLE_CONFIGS = [
    {
        "raw_path": f"{DATA_DIR}/olist_orders_{FILE_SUFFIX}.csv",
        "table_name": "orders",
    },
    {
        "raw_path": f"{DATA_DIR}/olist_customers_{FILE_SUFFIX}.csv",
        "table_name": "customers",
    },
    {
        "raw_path": f"{DATA_DIR}/olist_order_items_{FILE_SUFFIX}.csv",
        "table_name": "order_items",
    },
    {
        "raw_path": f"{DATA_DIR}/olist_order_payments_{FILE_SUFFIX}.csv",
        "table_name": "payments",
    },
    {
        "raw_path": f"{DATA_DIR}/olist_products_{FILE_SUFFIX}.csv",
        "table_name": "products",
    },
    {
    "raw_path": f"{DATA_DIR}/product_category_name_translation.csv",
    "table_name": "product_category_translation",
   },
]


logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main() -> None:
    """Run ETL pipeline for multiple ecommerce datasets."""
    try:
        logging.info(f"Multi-table ETL pipeline started. DATA_MODE={DATA_MODE}")

        for config in TABLE_CONFIGS:
            raw_path = config["raw_path"]
            table_name = config["table_name"]

            logging.info(f"Processing table: {table_name}")
            logging.info(f"Source file: {raw_path}")

            raw_df = extract_data(raw_path)
            logging.info(f"{table_name}: Raw rows: {len(raw_df)}")

            clean_df = transform_data(raw_df)
            logging.info(f"{table_name}: Clean rows: {len(clean_df)}")

            load_data_to_sqlite(clean_df, DB_PATH, table_name)
            logging.info(f"{table_name}: Loaded to SQLite.")

        logging.info("Building analytics_sales table started.")
        build_analytics_table(DB_PATH, ANALYTICS_SQL_PATH)
        logging.info("analytics_sales table built successfully.")

        logging.info("Multi-table ETL pipeline completed successfully.")
        print("Multi-table ETL pipeline completed successfully.")
        print(f"DATA_MODE={DATA_MODE}")

    except Exception as error:
        logging.exception("Multi-table ETL pipeline failed.")
        print(f"Multi-table ETL pipeline failed: {error}")


if __name__ == "__main__":
    main()