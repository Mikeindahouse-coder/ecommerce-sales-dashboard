WITH first_purchase AS (
    SELECT c.customer_unique_id,
    MIN(STRFTIME('%Y-%m', o.order_purchase_timestamp)) AS first_order_month
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
),
monthly_customers AS (
    SELECT DISTINCT c.customer_unique_id,
    STRFTIME('%Y-%m', o.order_purchase_timestamp) AS order_month
    FROM orders o
    JOIN customers c ON c.customer_id = o.customer_id
),
long_sheet AS (
    SELECT f.first_order_month, 
    (CAST(STRFTIME('%Y', m.order_month || '-01') AS INT) - CAST(STRFTIME('%Y', f.first_order_month || '-01') AS INT)) * 12
    + (CAST(STRFTIME('%m', m.order_month || '-01') AS INT) - CAST(STRFTIME('%m', f.first_order_month || '-01') AS INT)) AS month_number,
    COUNT(*) AS customers
    FROM first_purchase f
    LEFT JOIN monthly_customers m ON f.customer_unique_id = m.customer_unique_id
    GROUP BY f.first_order_month, month_number
)
SELECT l.first_order_month, l.month_number, l.customers,
ROUND(l.customers * 100.0 / t.customers, 2) AS cohort_retention_rate
FROM long_sheet l
JOIN long_sheet t ON l.first_order_month = t.first_order_month
AND t.month_number = 0
ORDER BY l.first_order_month, l.month_number;