-- TASK 1

-- sudo docker-compose --env-file ./.env.list exec db psql -U postgres -c "CREATE DATABASE shop;"

CREATE TABLE IF NOT EXISTS order_status(
    order_status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    _password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff SMALLINT,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);

CREATE TABLE IF NOT EXISTS carts(
    cart_id SERIAL PRIMARY KEY,
    users_user_id INT,
    subtotal DECIMAL,
    total DECIMAL,
    _timestamp TIMESTAMP(2),
    CONSTRAINT fk_user_id
        FOREIGN KEY(users_user_id)
            REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS _order(
    order_id SERIAL PRIMARY KEY,
    carts_cart_id INT,
    order_status_order_status_id INT,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),
    CONSTRAINT fk_cart_id
        FOREIGN KEY(carts_cart_id)
            REFERENCES carts(cart_id),
    CONSTRAINT fk_order_status_id
        FOREIGN KEY(order_status_order_status_id)
            REFERENCES order_status(order_status_id)
);

CREATE TABLE IF NOT EXISTS categories(
    category_id SERIAL PRIMARY KEY,
    category_title VARCHAR(255),
    category_description TEXT
);

CREATE TABLE IF NOT EXISTS products(
    product_id SERIAL PRIMARY KEY,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(255),
    category_id INT,
    CONSTRAINT fk_category_id
        FOREIGN KEY(category_id)
            REFERENCES categories(category_id)
);

CREATE TABLE IF NOT EXISTS cart_product(
    carts_cart_id INT,
    products_product_id INT,
    CONSTRAINT fk_cart_id
        FOREIGN KEY(carts_cart_id)
            REFERENCES carts(cart_id),
    CONSTRAINT fk_product_id
        FOREIGN KEY(products_product_id)
            REFERENCES products(product_id)
);

-- sudo docker cp ./order_statuses.csv docker-db-1:/usr/src/order_statuses.csv
-- sudo docker cp ./users.csv docker-db-1:/usr/src/users.csv
-- sudo docker cp ./carts.csv docker-db-1:/usr/src/carts.csv
-- sudo docker cp ./orders.csv docker-db-1:/usr/src/orders.csv
-- sudo docker cp ./categories.csv docker-db-1:/usr/src/categories.csv
-- sudo docker cp ./products.csv docker-db-1:/usr/src/products.csv
-- sudo docker cp ./cart_products.csv docker-db-1:/usr/src/cart_products.csv

COPY order_status(
    order_status_id,
    status_name)
FROM '/usr/src/order_statuses.csv'
DELIMITER ',';

COPY users(
    user_id,
    email,
    _password,
    first_name,
    last_name,
    middle_name,
    is_staff,
    country,
    city,
    address
    )
FROM '/usr/src/users.csv'
DELIMITER ',';

COPY carts(
    cart_id,
    users_user_id,
    subtotal,
    total,
    _timestamp
    )
FROM '/usr/src/carts.csv'
DELIMITER ',';

COPY _order(
    order_id,
    carts_cart_id,
    order_status_order_status_id,
    shipping_total,
    total,
    created_at,
    updated_at
    )
FROM '/usr/src/orders.csv'
DELIMITER ',';

COPY categories(
    category_id,
    category_title,
    category_description
    )
FROM '/usr/src/categories.csv'
DELIMITER ',';

COPY products(
    product_id,
    product_title,
    product_description,
    in_stock,
    price,
    slug,
    category_id
    )
FROM '/usr/src/products.csv'
DELIMITER ',';

COPY cart_product(
    carts_cart_id,
    products_product_id
    )
FROM '/usr/src/cart_products.csv'
DELIMITER ',';

-- TASK 2

ALTER TABLE users ADD COLUMN phone_number INT;

ALTER TABLE users ALTER COLUMN phone_number TYPE VARCHAR;

-- TASK 3

UPDATE products SET price = price * 2;
