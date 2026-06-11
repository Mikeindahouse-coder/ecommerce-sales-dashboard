import pandas as pd

files = [
    "olist_orders_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_products_dataset.csv",
    "product_category_name_translation.csv"
]

for file in files:

    raw_path = "data/raw/" + file

    df = pd.read_csv(raw_path)

    sample_df = df.head(100)

    sample_file = file.replace(
        "dataset",
        "sample"
    )

    sample_path = "data/sample/" + sample_file

    sample_df.to_csv(
        sample_path,
        index=False
    )

    print(f"Created: {sample_file}")

