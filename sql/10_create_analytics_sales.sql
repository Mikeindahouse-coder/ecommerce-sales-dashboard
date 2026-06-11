DROP TABLE IF EXISTS analytics_sales;

CREATE TABLE analytics_sales AS
WITH payment_summary AS (
    SELECT
        order_id,
        SUM(payment_value) AS total_payment_value,
        COUNT(*) AS payment_count
    FROM payments
    GROUP BY order_id
)
SELECT
    o.order_id,
    o.customer_id,
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    o.order_status,
    o.order_purchase_timestamp,
    oi.order_item_id,
    oi.product_id,
    p.product_category_name,
    t.product_category_name_english,
    oi.seller_id,
    oi.price,
    oi.freight_value,
    ps.total_payment_value,
    ps.payment_count
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
LEFT JOIN order_items AS oi
    ON o.order_id = oi.order_id
LEFT JOIN products AS p
    ON oi.product_id = p.product_id
LEFT JOIN product_category_translation AS t
    ON p.product_category_name = t.product_category_name
LEFT JOIN payment_summary AS ps
    ON o.order_id = ps.order_id;