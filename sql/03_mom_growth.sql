WITH monthly AS (
    SELECT STRFTIME('%Y-%m', o.order_purchase_timestamp) AS ym,
    SUM(s.price) AS monthly_revenue
    FROM orders o
    JOIN order_items s ON o.order_id = s.order_id
    GROUP BY ym
),
filtered_monthly AS ( 
    SELECT ym, monthly_revenue,
    LAG(monthly_revenue) OVER (ORDER BY ym) AS previous_month_revenue
    FROM monthly
    WHERE ym BETWEEN '2017-01' AND '2018-08'
)
SELECT ym, ROUND(monthly_revenue, 2) AS monthly_revenue,
ROUND(previous_month_revenue, 2) AS previous_month_revenue,
ROUND((monthly_revenue - previous_month_revenue) / previous_month_revenue * 100, 2) AS mom_growth_pct
FROM filtered_monthly
ORDER BY ym;