BEGIN;
INSERT INTO potential_customers (email, _name, surname, second_name, city)
VALUES
    ('email12@gmail.com', 'first_name 12', 'last_name 12', 'middle_name 12', 'city 12'),
    ('email2@gmail.com', 'first_name 2', 'last_name 2', 'middle_name 2', 'city 2');
SELECT * FROM potential_customers;
ROLLBACK;
END;

SELECT * FROM potential_customers;

BEGIN;
UPDATE potential_customers SET _name = 'first_name 18' WHERE id = 6;
SAVEPOINT set_name;
UPDATE potential_customers SET city = 'city 17' WHERE city = 'city 12';
SAVEPOINT set_city;
UPDATE potential_customers SET city = 'city 5' WHERE city = 'city 12';
SAVEPOINT set_city;
SELECT * FROM potential_customers;
ROLLBACK TO SAVEPOINT set_city;
COMMIT;
END;

SELECT * FROM potential_customers;

BEGIN;
DELETE FROM potential_customers
WHERE city = 'city 17';
SAVEPOINT city_del;
DELETE FROM potential_customers
WHERE id = 6;
SELECT * FROM potential_customers;
ROLLBACK TO SAVEPOINT city_del;
COMMIT;
END;

SELECT * FROM potential_customers;

--

BEGIN;
-- SELECT setval(pg_get_serial_sequence('users', 'user_id'), coalesce(max(user_id)+1, 1), false) FROM users;
INSERT INTO users (email, _password, first_name, last_name, middle_name, is_staff, country, city, address)
VALUES
    ('email@gmail.com',
     '895343', 'first_name',
     'last_name',
     'middle_name',
     '0',
     'country',
     'city',
     'address'),
    ('email4563@gmail.com',
     '1424643',
     'first_name4563',
     'last_name4563',
     'middle_name4563',
     '1',
     'country4563',
     'city4563',
     'address4563'),
    ('email5200@gmail.com',
     '24526343',
     'first_name5200',
     'last_name5200',
     'middle_name5200',
     '0',
     'country5200',
     'city5200',
     'address5200');
SAVEPOINT set_users;
UPDATE users SET is_staff = '1' WHERE user_id < 500;
DELETE FROM users
WHERE user_id > 3000;
SELECT * FROM users;
ROLLBACK TO SAVEPOINT set_users;
COMMIT;
END;

SELECT * FROM users;

--

BEGIN;
INSERT INTO cart_product (carts_cart_id, products_product_id)
VALUES
    (343, 500),
    (520, 36),
    (78, 254);
SAVEPOINT set_prod;
UPDATE cart_product SET products_product_id = '45' WHERE carts_cart_id = '343';
DELETE FROM cart_product
WHERE carts_cart_id = '343';
SAVEPOINT del_343;
INSERT INTO cart_product (carts_cart_id, products_product_id)
VALUES
    (343, 487);
SELECT * FROM cart_product;
ROLLBACK TO SAVEPOINT del_343;
COMMIT;
END;

SELECT * FROM cart_product;
