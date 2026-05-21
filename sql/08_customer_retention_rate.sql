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
)
SELECT f.first_order_month,
COUNT(DISTINCT f.customer_unique_id) AS cohort_size,
COUNT(DISTINCT m.customer_unique_id) AS retained_next_month,
ROUND(COUNT(DISTINCT m.customer_unique_id) * 100.0 / COUNT(DISTINCT f.customer_unique_id), 2) AS retention_rate
FROM first_purchase f
LEFT JOIN monthly_customers m
ON f.customer_unique_id = m.customer_unique_id
AND m.order_month = STRFTIME('%Y-%m', DATE(f.first_order_month || '-01', '+1 month'))
GROUP BY f.first_order_month
ORDER BY f.first_order_month;