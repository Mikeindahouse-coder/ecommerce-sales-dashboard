WITH totaldata AS (
    SELECT c.customer_unique_id, COUNT(DISTINCT o.order_id) AS orders_num
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)
SELECT SUM(CASE WHEN orders_num > 1 THEN 1 ELSE 0 END) AS repeat_customer,
COUNT(*) AS total_customer,
ROUND(SUM(CASE WHEN orders_num > 1 THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS repeat_customer_rate
FROM totaldata;