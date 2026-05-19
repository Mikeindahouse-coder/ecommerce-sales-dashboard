WITH november_orders AS (
    SELECT order_id, STRFTIME('%Y-%m', order_purchase_timestamp) AS ym
    FROM orders
)
SELECT COALESCE(t.product_category_name_english, 'Unknown') AS category_name,
ROUND(SUM(oi.price), 2) AS monthly_revenue,
COUNT(DISTINCT no.order_id) AS order_count,
ROUND(SUM(oi.price) / COUNT(DISTINCT no.order_id), 2) AS avg_order_value
FROM november_orders no
JOIN order_items oi ON no.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN product_category_translation t ON p.product_category_name = t.product_category_name
WHERE no.ym = '2017-11'
GROUP BY COALESCE(t.product_category_name_english, 'Unknown')
ORDER BY monthly_revenue DESC;