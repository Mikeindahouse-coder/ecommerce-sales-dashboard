import sqlite3
from pathlib import Path

import pandas as pd


DB_PATH = Path("olist_ecommerce.db")
#sql/01_monthly_revenue.sql
#sql/02_category_revenue.sql
#sql/03_mom_growth.sql
#sql/04_aov_analysis.sql
#sql/05_customer_first_purchase.sql
#06_repeat_customer_rate.sql
#07_new_vs_repeat_customers_by_month.sql
#08_customer_retention_rate.sql
#09_cohort_retention_matrix.sql
#10_create_analytics_sales.sql
SQL_PATH = Path("sql/04_aov_analysis.sql")

def main() -> None:
    query = SQL_PATH.read_text(encoding="utf-8")

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(query, conn)

    print(df)


if __name__ == "__main__":
    main()