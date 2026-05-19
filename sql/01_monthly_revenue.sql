WITH monthly AS (
    SELECT STRFTIME('%Y-%m', o.order_purchase_timestamp) AS ym,
    SUM(s.price) AS monthly_revenue,
    COUNT(DISTINCT o.order_id) AS order_count
    FROM orders o
    JOIN order_items s ON o.order_id = s.order_id
    GROUP BY ym
)
SELECT ym, ROUND(monthly_revenue, 2) AS monthly_revenue,
    order_count, ROUND(monthly_revenue / order_count, 2) AS avg_order_value
    FROM monthly
    WHERE ym BETWEEN '2017-01' AND '2018-08'
    ORDER BY ym;