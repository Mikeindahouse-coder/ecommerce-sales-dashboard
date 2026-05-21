# E-Commerce Sales Dashboard

## Project Objective

Build an end-to-end business intelligence project using SQL, Python, SQLite, and Power BI to analyze e-commerce revenue trends, product performance, customer behavior, regional sales distribution, and order fulfillment status.

---

## Tools

- SQL (SQLite)
- Python
- pandas
- Power BI

---

## Dataset

Dataset: Olist Brazilian E-Commerce Dataset  
Source: Kaggle

---

## Business Questions

- What are the major revenue trends over time?
- Which product categories contribute the most revenue?
- Is revenue growth driven more by order volume or average order value?
- Which customer states contribute the most revenue?
- What is the overall order delivery performance?
- How strong is customer retention and repeat purchasing behavior?

---

## Dashboard Preview

![Dashboard Preview](dashboard/dashboard_preview.png)

---

## Key Business Insights

### Revenue Trends

- Revenue growth accelerated significantly from 2017 to mid-2018.
- November 2017 recorded the highest monthly revenue.
- Revenue growth was mainly driven by increased order volume rather than higher average order value (AOV).

### Product Performance

- health_beauty generated the highest total revenue.
- computers had the highest average order value.
- Top categories consistently dominated platform sales.

### Customer Behavior

- New customer acquisition increased rapidly during the platform growth period.
- Repeat customer rate remained relatively low.
- Most customer cohorts showed next-month retention below 1%.

### Operational Insights

- Over 98% of orders were successfully delivered.
- São Paulo (SP) contributed the highest regional revenue.

---

## SQL Analysis

| File | Description |
|---|---|
| 01_monthly_revenue.sql | Analyze monthly revenue trend |
| 02_category_revenue.sql | Identify top revenue-generating categories |
| 03_mom_growth.sql | Calculate month-over-month revenue growth |
| 04_aov_analysis.sql | Analyze average order value trends |
| 05_customer_first_purchase.sql | Find customer first purchase month |
| 06_repeat_customer_rate.sql | Calculate repeat customer rate |
| 07_new_vs_repeat_customers_by_month.sql | Compare new and repeat customers over time |
| 08_customer_retention_rate.sql | Calculate next-month customer retention |
| 09_cohort_retention_matrix.sql | Build cohort retention matrix |

---

## Project Structure

```text
data/        -> raw CSV dataset
sql/         -> SQL analysis scripts
scripts/     -> Python scripts for loading and running queries
dashboard/   -> Power BI dashboard and preview image
notebooks/   -> optional analysis notebooks