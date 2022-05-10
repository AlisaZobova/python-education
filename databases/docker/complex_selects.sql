-- TASK 1

CREATE TABLE IF NOT EXISTS potential_customers(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    _name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255)
);

--

INSERT INTO potential_customers (email, _name, surname, second_name, city)
VALUES('email1@gmail.com', 'first_name 1', 'last_name 1', 'middle_name 1', 'city 1'),
      ('email3@gmail.com', 'first_name 3', 'last_name 3', 'middle_name 3', 'city 17'),
      ('email5@gmail.com', 'first_name 5', 'last_name 5', 'middle_name 5', 'city 5'),
      ('email6@gmail.com', 'first_name 6', 'last_name 6', 'middle_name 6', 'city 17'),
      ('email9@gmail.com', 'first_name 9', 'last_name 9', 'middle_name 9', 'city 9'),
      ('email17@gmail.com', 'first_name 17', 'last_name 17', 'middle_name 17', 'city 17'),
      ('email25@gmail.com', 'first_name 25', 'last_name 25', 'middle_name 25', 'city 17');

--

SELECT _name, email
FROM potential_customers
WHERE city = 'city 17'
UNION ALL
SELECT first_name, email
FROM users
WHERE city = 'city 17';

-- TASK 2

SELECT first_name, email
FROM users
ORDER BY city, first_name;

-- TASK 3

SELECT category_id, SUM(in_stock) as sum_in_stock
FROM products
GROUP BY products.category_id
ORDER BY SUM(in_stock) DESC;

-- TASK 4

SELECT products.product_title
FROM products
LEFT JOIN cart_product ON products.product_id = cart_product.products_product_id
WHERE cart_product.products_product_id is NULL;

--

SELECT products.product_title
FROM products
    LEFT JOIN cart_product
        JOIN _order
        ON cart_product.carts_cart_id = _order.carts_cart_id
    ON products.product_id = cart_product.products_product_id
    WHERE cart_product.products_product_id is NULL;

--

SELECT products_product_id as product_id, COUNT(products_product_id)
FROM cart_product
GROUP BY products_product_id
ORDER BY COUNT(products_product_id) DESC
LIMIT 10;

--

SELECT products.product_title, COUNT(products.product_title)
FROM products
    JOIN cart_product
        JOIN _order
        ON cart_product.carts_cart_id = _order.carts_cart_id
    ON products.product_id = cart_product.products_product_id
GROUP BY products.product_title
ORDER BY COUNT(products.product_title) DESC
LIMIT 10;

--

-- IF USER CAN HAVE SEVERAL ORDERS

SELECT carts.users_user_id, MAX(_order.total)
FROM _order
    JOIN carts
        JOIN users
        ON carts.users_user_id = users.user_id
    ON _order.carts_cart_id = carts.cart_id
GROUP BY carts.users_user_id
ORDER BY MAX(_order.total) DESC
LIMIT 5;

-- IF USER CAN HAVE ONLY ONE ORDER

SELECT carts.users_user_id, _order.total
FROM _order
    JOIN carts
        JOIN users
        ON carts.users_user_id = users.user_id
    ON _order.carts_cart_id = carts.cart_id
ORDER BY _order.total DESC
LIMIT 5;

--

SELECT carts.users_user_id, COUNT(carts.cart_id)
FROM carts
    INNER JOIN _order
    ON carts.cart_id = _order.carts_cart_id
GROUP BY carts.users_user_id
ORDER BY COUNT(carts.cart_id) DESC
LIMIT 5;

--

SELECT carts.users_user_id, COUNT(carts.cart_id)
FROM carts
    LEFT JOIN _order
    ON carts.cart_id = _order.carts_cart_id
    WHERE _order.carts_cart_id is NULL
GROUP BY carts.users_user_id
ORDER BY COUNT(carts.cart_id) DESC
LIMIT 5;
