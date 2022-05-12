-- INSERTS

INSERT INTO cart_product
SELECT i, i*2
FROM generate_series(1, 2000) as i;

INSERT INTO cart_product
SELECT i, i
FROM generate_series(1, 2000) as i;

SELECT setval(pg_get_serial_sequence('products', 'product_id'), coalesce(max(product_id)+1, 1), false) FROM products;
INSERT INTO products (product_title, product_description, in_stock, price, slug, category_id)
SELECT product_title, product_description, in_stock, price, slug, category_id FROM products;

SELECT setval(pg_get_serial_sequence('_order', 'order_id'), coalesce(max(order_id)+1, 1), false) FROM _order;
INSERT INTO _order (carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at)
SELECT carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at from _order;

SELECT setval(pg_get_serial_sequence('carts', 'cart_id'), coalesce(max(cart_id)+1, 1), false) FROM carts;
INSERT INTO carts (users_user_id, subtotal, total, _timestamp)
SELECT users_user_id, subtotal, total, _timestamp FROM carts;

SELECT setval(pg_get_serial_sequence('users', 'user_id'), coalesce(max(user_id)+1, 1), false) FROM users;
INSERT INTO users (email, _password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number)
SELECT email, _password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number from users;

--INDEXES

CREATE INDEX idx_products_product_title ON products(product_title);
CREATE INDEX idx_cart_product_products_product_id ON cart_product(products_product_id);
CREATE INDEX idx_cart_product_carts_cart_id ON cart_product(carts_cart_id);
CREATE INDEX idx_order_carts_cart_id ON _order(carts_cart_id);

CREATE INDEX idx_carts_users_user_id ON carts(users_user_id);
CREATE INDEX idx_order_total ON _order(total);

DROP INDEX idx_products_product_title;
DROP INDEX idx_cart_product_products_product_id;
DROP INDEX idx_cart_product_carts_cart_id;
DROP INDEX idx_order_carts_cart_id;

DROP INDEX idx_carts_users_user_id;
DROP INDEX idx_order_total;

-- CREATE INDEX idx_cart_product_products_product_id ON cart_product USING HASH(products_product_id);
-- CREATE INDEX idx_cart_product_carts_cart_id ON cart_product USING HASH(carts_cart_id);
-- CREATE INDEX idx_order_carts_cart_id ON _order USING HASH(carts_cart_id);

-- QUERIES

EXPLAIN ANALYSE
SELECT products.product_title, COUNT(products.product_title)
FROM products
    JOIN cart_product
        JOIN _order
        ON cart_product.carts_cart_id = _order.carts_cart_id
    ON products.product_id = cart_product.products_product_id
GROUP BY products.product_title
LIMIT 10;

-- WITHOUT INDEXES
-- Limit  (cost=335676.93..335679.46 rows=10 width=20) (actual time=35709.387..35714.350 rows=10 loops=1)
--   ->  Finalize GroupAggregate  (cost=335676.93..336690.83 rows=4002 width=20) (actual time=35686.662..35691.595 rows=10 loops=1)
--         Group Key: products.product_title
--         ->  Gather Merge  (cost=335676.93..336610.79 rows=8004 width=20) (actual time=35686.635..35691.523 rows=31 loops=1)
--               Workers Planned: 2
--               Workers Launched: 2
--               ->  Sort  (cost=334676.91..334686.91 rows=4002 width=20) (actual time=35639.561..35640.153 rows=486 loops=3)
--                     Sort Key: products.product_title
--                     Sort Method: quicksort  Memory: 390kB
--                     Worker 0:  Sort Method: quicksort  Memory: 390kB
--                     Worker 1:  Sort Method: quicksort  Memory: 390kB
--                     ->  Partial HashAggregate  (cost=334397.44..334437.46 rows=4002 width=20) (actual time=35620.640..35626.114 rows=3753 loops=3)
--                           Group Key: products.product_title
--                           Batches: 1  Memory Usage: 721kB
--                           Worker 0:  Batches: 1  Memory Usage: 721kB
--                           Worker 1:  Batches: 1  Memory Usage: 721kB
--                           ->  Parallel Hash Join  (cost=4916.72..190463.63 rows=28786762 width=12) (actual time=427.443..18665.651 rows=11241000 loops=3)
--                                 Hash Cond: (_order.carts_cart_id = cart_product.carts_cart_id)
--                                 ->  Parallel Seq Scan on _order  (cost=0.00..38401.00 rows=1280000 width=4) (actual time=0.076..762.167 rows=500000 loops=3)
--                                 ->  Parallel Hash  (cost=4682.39..4682.39 rows=18746 width=16) (actual time=426.929..426.941 rows=14997 loops=3)
--                                       Buckets: 65536  Batches: 1  Memory Usage: 2912kB
--                                       ->  Merge Join  (cost=4128.47..4682.39 rows=18746 width=16) (actual time=189.341..390.367 rows=14997 loops=3)
--                                             Merge Cond: (products.product_id = cart_product.products_product_id)
--                                             ->  Parallel Index Scan using products_pkey on products  (cost=0.42..17064.00 rows=213333 width=16) (actual time=0.080..3.297 rows=1334 loops=3)
--                                             ->  Sort  (cost=4127.02..4239.50 rows=44990 width=8) (actual time=168.339..256.420 rows=44990 loops=3)
--                                                   Sort Key: cart_product.products_product_id
--                                                   Sort Method: quicksort  Memory: 3475kB
--                                                   Worker 0:  Sort Method: quicksort  Memory: 3475kB
--                                                   Worker 1:  Sort Method: quicksort  Memory: 3475kB
--                                                   ->  Seq Scan on cart_product  (cost=0.00..649.90 rows=44990 width=8) (actual time=0.042..81.503 rows=44990 loops=3)
-- Planning Time: 0.493 ms
-- JIT:
--   Functions: 64
-- "  Options: Inlining false, Optimization false, Expressions true, Deforming true"
-- "  Timing: Generation 8.861 ms, Inlining 0.000 ms, Optimization 3.208 ms, Emission 53.302 ms, Total 65.371 ms"
-- Execution Time: 35718.777 ms

--

-- WITH INDEXES
-- Limit  (cost=1001.16..2907.88 rows=10 width=20) (actual time=329.992..1108.164 rows=10 loops=1)
--   ->  Finalize GroupAggregate  (cost=1001.16..764068.95 rows=4002 width=20) (actual time=329.987..1108.123 rows=10 loops=1)
--         Group Key: products.product_title
--         ->  Gather Merge  (cost=1001.16..763988.91 rows=8004 width=20) (actual time=187.920..1108.041 rows=11 loops=1)
--               Workers Planned: 2
--               Workers Launched: 2
--               ->  Partial GroupAggregate  (cost=1.14..762065.02 rows=4002 width=20) (actual time=104.536..998.265 rows=11 loops=3)
--                     Group Key: products.product_title
--                     ->  Nested Loop  (cost=1.14..691741.75 rows=14056650 width=12) (actual time=0.414..749.583 rows=141334 loops=3)
--                           ->  Nested Loop  (cost=0.71..165974.48 rows=18746 width=16) (actual time=0.336..12.944 rows=153 loops=3)
--                                 ->  Parallel Index Scan using idx_products_product_title on products  (cost=0.42..33289.69 rows=213333 width=16) (actual time=0.230..4.170 rows=1367 loops=3)
--                                 ->  Index Scan using idx_cart_product_products_product_id on cart_product  (cost=0.29..0.50 rows=12 width=8) (actual time=0.002..0.003 rows=0 loops=4102)
--                                       Index Cond: (products_product_id = products.product_id)
--                           ->  Index Only Scan using idx_order_carts_cart_id on _order  (cost=0.43..18.05 rows=1000 width=4) (actual time=0.013..1.639 rows=924 loops=459)
--                                 Index Cond: (carts_cart_id = cart_product.carts_cart_id)
--                                 Heap Fetches: 0
-- Planning Time: 1.318 ms
-- Execution Time: 1108.280 ms

EXPLAIN ANALYSE
SELECT carts.users_user_id, _order.total
FROM _order
    JOIN carts
        JOIN users
        ON carts.users_user_id = users.user_id
    ON _order.carts_cart_id = carts.cart_id
    LIMIT 5000;

-- WITHOUT INDEXES

-- Limit  (cost=478.30..1063.92 rows=5000 width=10) (actual time=39.601..96.742 rows=5000 loops=1)
--   ->  Nested Loop  (cost=478.30..11722.21 rows=96000 width=10) (actual time=39.597..85.925 rows=5000 loops=1)
--         ->  Hash Join  (cost=478.00..2490.01 rows=96000 width=10) (actual time=39.572..57.879 rows=5000 loops=1)
--               Hash Cond: (_order.carts_cart_id = carts.cart_id)
--               ->  Seq Scan on _order  (cost=0.00..1760.00 rows=96000 width=10) (actual time=0.006..5.719 rows=5000 loops=1)
--               ->  Hash  (cost=278.00..278.00 rows=16000 width=8) (actual time=39.549..39.552 rows=16000 loops=1)
--                     Buckets: 16384  Batches: 1  Memory Usage: 753kB
--                     ->  Seq Scan on carts  (cost=0.00..278.00 rows=16000 width=8) (actual time=0.004..19.331 rows=16000 loops=1)
--         ->  Memoize  (cost=0.30..0.44 rows=1 width=4) (actual time=0.002..0.002 rows=1 loops=5000)
--               Cache Key: carts.users_user_id
--               Cache Mode: logical
--               Hits: 3500  Misses: 1500  Evictions: 0  Overflows: 0  Memory Usage: 153kB
--               ->  Index Only Scan using users_pkey on users  (cost=0.29..0.43 rows=1 width=4) (actual time=0.002..0.002 rows=1 loops=1500)
--                     Index Cond: (user_id = carts.users_user_id)
--                     Heap Fetches: 0
-- Planning Time: 0.207 ms
-- Execution Time: 102.302 ms

--

-- WITH INDEXES
-- Limit  (cost=0.86..445.11 rows=5000 width=10) (actual time=0.055..32.675 rows=5000 loops=1)
--   ->  Merge Join  (cost=0.86..8530.29 rows=96000 width=10) (actual time=0.051..21.338 rows=5000 loops=1)
--         Merge Cond: (carts.cart_id = _order.carts_cart_id)
--         ->  Nested Loop  (cost=0.57..7377.15 rows=16000 width=8) (actual time=0.031..0.991 rows=79 loops=1)
--               ->  Index Scan using carts_pkey on carts  (cost=0.29..545.28 rows=16000 width=8) (actual time=0.014..0.170 rows=79 loops=1)
--               ->  Index Only Scan using users_pkey on users  (cost=0.29..0.43 rows=1 width=4) (actual time=0.005..0.005 rows=1 loops=79)
--                     Index Cond: (user_id = carts.users_user_id)
--                     Heap Fetches: 0
--         ->  Index Scan using idx_order_carts_cart_id on _order  (cost=0.29..2567.29 rows=96000 width=10) (actual time=0.011..8.239 rows=5000 loops=1)
-- Planning Time: 0.928 ms
-- Execution Time: 38.518 ms


EXPLAIN ANALYSE
SELECT products.product_title
FROM products
    LEFT JOIN cart_product
        JOIN _order
        ON cart_product.carts_cart_id = _order.carts_cart_id
    ON products.product_id = cart_product.products_product_id
    WHERE cart_product.products_product_id > 15000;

-- WITHOUT INDEXES
-- Nested Loop  (cost=389.88..2646.36 rows=2 width=12) (actual time=4.137..4.152 rows=0 loops=1)
--   ->  Hash Join  (cost=389.46..2629.48 rows=2 width=4) (actual time=4.133..4.145 rows=0 loops=1)
--         Hash Cond: (_order.carts_cart_id = cart_product.carts_cart_id)
--         ->  Seq Scan on _order  (cost=0.00..1760.00 rows=96000 width=4) (actual time=0.008..0.010 rows=1 loops=1)
--         ->  Hash  (cost=389.44..389.44 rows=2 width=8) (actual time=4.116..4.121 rows=0 loops=1)
--               Buckets: 1024  Batches: 1  Memory Usage: 8kB
--               ->  Seq Scan on cart_product  (cost=0.00..389.44 rows=2 width=8) (actual time=4.112..4.113 rows=0 loops=1)
--                     Filter: (products_product_id > 15000)
--                     Rows Removed by Filter: 22995
--   ->  Index Scan using products_pkey on products  (cost=0.42..8.44 rows=1 width=16) (never executed)
--         Index Cond: (product_id = cart_product.products_product_id)
-- Planning Time: 0.570 ms
-- Execution Time: 4.201 ms

--

-- WITH INDEXES
-- Nested Loop  (cost=1.00..25.07 rows=1 width=12) (actual time=0.011..0.020 rows=0 loops=1)
--   ->  Nested Loop  (cost=0.71..16.75 rows=1 width=16) (actual time=0.008..0.013 rows=0 loops=1)
--         ->  Index Scan using idx_cart_product_products_product_id on cart_product  (cost=0.29..8.30 rows=1 width=8) (actual time=0.005..0.007 rows=0 loops=1)
--               Index Cond: (products_product_id > 15000)
--         ->  Index Scan using products_pkey on products  (cost=0.42..8.44 rows=1 width=16) (never executed)
--               Index Cond: (product_id = cart_product.products_product_id)
--   ->  Index Only Scan using idx_order_carts_cart_id on _order  (cost=0.29..8.31 rows=1 width=4) (never executed)
--         Index Cond: (carts_cart_id = cart_product.carts_cart_id)
--         Heap Fetches: 0
-- Planning Time: 0.663 ms
-- Execution Time: 0.057 ms
