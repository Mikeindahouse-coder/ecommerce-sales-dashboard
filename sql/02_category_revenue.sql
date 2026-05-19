SELECT COALESCE(t.product_category_name_english, 'Unknown') AS category_name,
ROUND(SUM(s.price), 2) AS total_revenue,
COUNT(DISTINCT o.order_id) AS order_count,
ROUND(SUM(s.price) / COUNT(DISTINCT o.order_id), 2) AS avg_order_value,
ROUND(SUM(s.price) / SUM(SUM(s.price)) OVER () * 100, 2) AS revenue_pct
FROM orders o
JOIN order_items s ON o.order_id = s.order_id
JOIN products p ON s.product_id = p.product_id
LEFT JOIN product_category_translation t ON p.product_category_name = t.product_category_name
GROUP BY category_name
ORDER BY total_revenue DESC;