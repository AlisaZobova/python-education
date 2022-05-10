-- TASK 1

SELECT *
FROM users;

SELECT first_name || ' ' || last_name || ' ' || middle_name as all_users
FROM users;

--

SELECT *
FROM products;

SELECT product_title as all_products
FROM products;

--

SELECT *
FROM order_status;

SELECT status_name as all_order_statuses
FROM order_status;

-- TASK 2

SELECT *
FROM _order
WHERE order_status_order_status_id IN (3, 4);

SELECT order_id
FROM _order
WHERE order_status_order_status_id IN (3, 4);

-- TASK 3

SELECT *
FROM products
WHERE price > 80 AND price <= 150;

SELECT *
FROM products
WHERE price BETWEEN 81 AND 150;

--

SELECT *
FROM _order
WHERE created_at > '2020-10-01';

SELECT *
FROM _order
WHERE created_at BETWEEN '2020-10-02' AND now();

--

SELECT *
FROM _order
WHERE created_at >= '2020-01-01'AND created_at < '2020-07-01';

SELECT *
FROM _order
WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30';

SELECT *
FROM _order
WHERE created_at >= '2020-01-01' AND created_at < timestamp '2020-01-01' + interval '6 months';

--

SELECT *
FROM products
WHERE category_id IN (7, 11, 18);

--

SELECT *
FROM _order
WHERE updated_at <= '2020-12-31' AND order_status_order_status_id != 4;

--

SELECT carts_cart_id, order_status_order_status_id
FROM _order
WHERE order_status_order_status_id = 5;

-- TASK 4

SELECT AVG(total) as average_sum
FROM _order
WHERE order_status_order_status_id = 4;

--

SELECT MAX(total) as max_sum
FROM _order
WHERE created_at >= '2020-07-01' AND created_at < timestamp '2020-07-01' + interval '3 months';
