# E-Commerce Sales Dashboard

## Project Overview

End-to-end Business Intelligence project built using SQL, Python, SQLite, and Power BI.

This project analyzes revenue trends, product performance, customer behavior, customer retention, regional sales distribution, and order fulfillment performance using the Olist Brazilian E-Commerce dataset.

The objective is to transform raw transactional data into actionable business insights through data cleaning, SQL analytics, and interactive dashboard development.

---

## Dashboard Preview

![Dashboard Preview](dashboard/dashboard_preview.png)

---

## Business Questions

This project aims to answer the following business questions:

* What are the major revenue trends over time?
* Which product categories contribute the most revenue?
* Is revenue growth driven more by order volume or average order value (AOV)?
* Which customer states contribute the most revenue?
* What is the overall order delivery performance?
* How strong is customer retention and repeat purchasing behavior?

---

## Data Pipeline

```text
Raw CSV Dataset
        ↓
Python Data Cleaning & Transformation
        ↓
SQLite Database
        ↓
SQL Business Analysis
        ↓
Analytics Tables
        ↓
Power BI Dashboard
        ↓
Business Insights
```

---

## Tools & Technologies

* SQL (SQLite)
* Python
* pandas
* SQLite
* Power BI

---

## Dataset

Dataset: Olist Brazilian E-Commerce Dataset

Source: Kaggle

The dataset contains information related to:

* Orders
* Customers
* Products
* Payments
* Sellers
* Order Reviews
* Delivery Information

---

## Dashboard Metrics

The dashboard tracks key business KPIs including:

* Total Revenue
* Total Orders
* Average Order Value (AOV)
* Monthly Revenue Trend
* Revenue Growth Rate
* Revenue by Product Category
* Revenue by Customer State
* New vs Repeat Customers
* Customer Retention Rate
* Order Delivery Performance

---

## Key Business Insights

### Revenue Trends

* Revenue increased significantly from 2017 to mid-2018.
* November 2017 recorded the highest monthly revenue.
* Revenue growth was primarily driven by increasing order volume rather than higher average order value (AOV).

### Product Performance

* Health & Beauty generated the highest total revenue.
* Computers achieved the highest average order value.
* A small number of product categories consistently contributed the majority of sales.

### Customer Behavior

* Customer acquisition grew rapidly during the platform expansion period.
* Repeat customer rates remained relatively low.
* Most customer cohorts exhibited next-month retention rates below 1%.

### Regional Analysis

* São Paulo (SP) generated the highest revenue contribution.
* Revenue was highly concentrated among several major states.

### Operational Performance

* More than 98% of orders were successfully delivered.
* Order fulfillment performance remained consistently strong throughout the analysis period.

---

## Business Analysis

### Revenue Analysis

* Monthly Revenue Trend
* Month-over-Month (MoM) Revenue Growth
* Average Order Value (AOV) Analysis

### Product Analysis

* Revenue by Product Category
* Top Revenue-Contributing Categories

### Customer Analysis

* First Purchase Analysis
* New vs Repeat Customer Analysis
* Repeat Purchase Rate
* Customer Retention Rate
* Cohort Retention Analysis

### Operations Analysis

* Order Status Analysis
* Delivery Performance Analysis

---

## SQL Analysis Scripts

| File                                    | Description                                |
| --------------------------------------- | ------------------------------------------ |
| 01_monthly_revenue.sql                  | Analyze monthly revenue trends             |
| 02_category_revenue.sql                 | Identify top revenue-generating categories |
| 03_mom_growth.sql                       | Calculate month-over-month revenue growth  |
| 04_aov_analysis.sql                     | Analyze average order value trends         |
| 05_customer_first_purchase.sql          | Find customer first purchase month         |
| 06_repeat_customer_rate.sql             | Calculate repeat customer rate             |
| 07_new_vs_repeat_customers_by_month.sql | Compare new and repeat customers over time |
| 08_customer_retention_rate.sql          | Calculate next-month retention rate        |
| 09_cohort_retention_matrix.sql          | Build customer cohort retention matrix     |

---

## Technical Highlights

* Built a relational SQLite database from raw CSV files.
* Developed reusable SQL queries for business analysis.
* Automated data cleaning and loading using Python and pandas.
* Performed customer retention and cohort analysis.
* Created business KPIs for revenue, customer behavior, and operations.
* Designed an interactive Power BI dashboard for stakeholder reporting.

---

## Business Impact

This dashboard enables business stakeholders to:

* Monitor revenue growth and sales performance.
* Identify high-performing product categories.
* Track customer acquisition and retention trends.
* Evaluate regional sales opportunities.
* Monitor operational delivery performance.
* Support data-driven business decisions.

---

## Project Results

* Analyzed over 100,000 e-commerce orders.
* Developed 9 business-focused SQL analysis modules.
* Built customer retention and cohort analysis frameworks.
* Identified key revenue-driving product categories.
* Determined that revenue growth was primarily driven by order volume rather than AOV.
* Integrated sales, customer, and operational metrics into a unified dashboard.

---

## Skills Demonstrated

### Data Analysis

* SQL
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Business Analytics

### Data Engineering

* ETL Pipeline Development
* SQLite Database Design
* Data Transformation

### Business Intelligence

* Power BI Dashboard Development
* KPI Design
* Customer Retention Analysis
* Cohort Analysis

### Programming

* Python
* pandas

---

## Project Structure

```text
ecommerce-sales-dashboard/
│
├── data/
│   └── raw dataset files
│
├── sql/
│   └── business analysis SQL scripts
│
├── scripts/
│   └── Python ETL and data processing scripts
│
├── dashboard/
│   ├── dashboard.pbix
│   └── dashboard_preview.png
│
├── notebooks/
│   └── exploratory analysis notebooks
│
└── README.md
```
