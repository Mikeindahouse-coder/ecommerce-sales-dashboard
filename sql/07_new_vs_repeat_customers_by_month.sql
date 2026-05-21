WITH first_purchase AS (
    SELECT c.customer_unique_id, MIN(STRFTIME('%Y-%m', o.order_purchase_timestamp)) AS first_order_month
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
),
monthly_customers AS (
    SELECT c.customer_unique_id, STRFTIME('%Y-%m', o.order_purchase_timestamp) AS order_month
    FROM orders o
    JOIN customers c ON c.customer_id = o.customer_id
)
SELECT m.order_month AS ym,
COUNT(DISTINCT CASE WHEN m.order_month = f.first_order_month THEN m.customer_unique_id END) AS new_customers,
COUNT(DISTINCT CASE WHEN m.order_month > f.first_order_month THEN m.customer_unique_id END) AS repeat_customers
FROM monthly_customers m
JOIN first_purchase f ON f.customer_unique_id = m.customer_unique_id
GROUP BY m.order_month
ORDER BY m.order_month;