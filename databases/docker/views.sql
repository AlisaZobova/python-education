CREATE OR REPLACE VIEW cheap_products AS
    SELECT product_title, price, category_id
    FROM products
    WHERE price < 100
    ORDER BY price
    WITH CHECK OPTION;

SELECT product_title, price FROM cheap_products;

DROP VIEW cheap_products CASCADE;

CREATE OR REPLACE VIEW canceled_orders AS
    SELECT _order.order_id, _order.carts_cart_id, _order.total, order_status.status_name
    FROM _order
        INNER JOIN order_status
            ON _order.order_status_order_status_id = order_status.order_status_id
    WHERE order_status_order_status_id = 5;

SELECT * FROM canceled_orders;

DROP VIEW canceled_orders;

CREATE OR REPLACE VIEW count_cheap_products_by_categories AS
    SELECT categories.category_title, COUNT(cheap_products.product_title)
    FROM cheap_products
        INNER JOIN categories
            ON cheap_products.category_id = categories.category_id
    GROUP BY categories.category_title
    ORDER BY COUNT(cheap_products.product_title) DESC;

SELECT * FROM count_cheap_products_by_categories;

DROP VIEW count_cheap_products_by_categories;

CREATE MATERIALIZED VIEW profit_by_products AS
    SELECT products.product_title, COUNT(cp.products_product_id) * products.price AS profit
    FROM products
        INNER JOIN cart_product cp
            ON products.product_id = cp.products_product_id
        INNER JOIN _order o
            ON cp.carts_cart_id = o.carts_cart_id
    WHERE order_status_order_status_id = 4
    GROUP BY products.product_title, products.price
    ORDER BY profit DESC
    WITH NO DATA;

REFRESH MATERIALIZED VIEW profit_by_products;

SELECT * FROM profit_by_products;

DROP MATERIALIZED VIEW profit_by_products;
