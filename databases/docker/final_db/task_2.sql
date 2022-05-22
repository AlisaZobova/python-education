-- SELECT query with meaningful use of different types of JOIN


BEGIN;

INSERT INTO car (branch_id, car_model_id, number, price)
SELECT branch_id, car_model_id, number, price
FROM car;

INSERT INTO rent (customer_id, car_id, date_of_renting, period_of_renting)
SELECT customer_id, car_id, date_of_renting, period_of_renting
FROM rent;

INSERT INTO customer (first_name, second_name, house_id, phone_number_id)
SELECT first_name, second_name, house_id, phone_number_id
FROM customer;

INSERT INTO branch (house_id, phone_number_id, branch_name)
SELECT house_id, phone_number_id, branch_name
FROM branch;

INSERT INTO car_model (car_brand_id, model)
SELECT car_brand_id, model
FROM car_model;

-- Displays 10 car numbers, customer names, and the number of times these customers rent those cars, in descending order

EXPLAIN ANALYZE
SELECT car.number, c.first_name, c.second_name, COUNT(*) as rent_count
FROM rent
    INNER JOIN car
        ON rent.car_id = car.car_id
    INNER JOIN customer c
        ON rent.customer_id = c.customer_id
GROUP BY car.number, c.first_name, c.second_name
-- index not working with descending sort,
-- but, I will leave it for the function,
-- since it makes it more visual,
-- but I will not use it in the analysis
-- ORDER BY COUNT(*) DESC
LIMIT 10;

CREATE INDEX car_number_idx ON car(number);
CREATE INDEX rent_customer_id_idx ON rent USING HASH(customer_id);
CREATE INDEX rent_car_id_idx ON rent USING HASH(car_id);
CREATE INDEX name_idx ON customer(first_name, second_name);

DROP INDEX IF EXISTS rent_customer_id_idx;
DROP INDEX IF EXISTS rent_car_id_idx;
DROP INDEX IF EXISTS car_number_idx;
DROP INDEX IF EXISTS name_idx;


-- WITHOUT INDEXES
--
-- Limit  (cost=13868.77..13870.94 rows=10 width=30) (actual time=124.449..127.881 rows=10 loops=1)
--   ->  GroupAggregate  (cost=13868.77..48609.89 rows=160000 width=30) (actual time=124.448..127.879 rows=10 loops=1)
-- "        Group Key: car.number, c.first_name, c.second_name"
--         ->  Incremental Sort  (cost=13868.77..45409.89 rows=160000 width=22) (actual time=124.414..127.828 rows=321 loops=1)
-- "              Sort Key: car.number, c.first_name, c.second_name"
--               Presorted Key: car.number
--               Full-sort Groups: 8  Sort Method: quicksort  Average Memory: 27kB  Peak Memory: 27kB
--               Pre-sorted Groups: 1  Sort Method: quicksort  Average Memory: 32kB  Peak Memory: 32kB
--               ->  Nested Loop  (cost=13862.93..36408.91 rows=160000 width=22) (actual time=124.382..127.647 rows=417 loops=1)
--                     ->  Gather Merge  (cost=13862.63..32097.92 rows=160000 width=13) (actual time=124.358..127.479 rows=417 loops=1)
--                           Workers Planned: 1
--                           Workers Launched: 1
--                           ->  Sort  (cost=12862.62..13097.91 rows=94118 width=13) (actual time=113.921..114.013 rows=938 loops=2)
--                                 Sort Key: car.number
--                                 Sort Method: external merge  Disk: 2032kB
--                                 Worker 0:  Sort Method: external merge  Disk: 1576kB
--                                 ->  Nested Loop  (cost=0.30..5087.45 rows=94118 width=13) (actual time=0.024..37.167 rows=80000 loops=2)
--                                       ->  Parallel Seq Scan on rent  (cost=0.00..2118.18 rows=94118 width=8) (actual time=0.004..4.318 rows=80000 loops=2)
--                                       ->  Memoize  (cost=0.30..0.34 rows=1 width=13) (actual time=0.000..0.000 rows=1 loops=160000)
--                                             Cache Key: rent.car_id
--                                             Cache Mode: logical
--                                             Hits: 86858  Misses: 3174  Evictions: 0  Overflows: 0  Memory Usage: 360kB
--                                             Worker 0:  Hits: 66794  Misses: 3174  Evictions: 0  Overflows: 0  Memory Usage: 360kB
--                                             ->  Index Scan using car_pkey on car  (cost=0.29..0.33 rows=1 width=13) (actual time=0.001..0.001 rows=1 loops=6348)
--                                                   Index Cond: (car_id = rent.car_id)
--                     ->  Memoize  (cost=0.30..0.32 rows=1 width=17) (actual time=0.000..0.000 rows=1 loops=417)
--                           Cache Key: rent.customer_id
--                           Cache Mode: logical
--                           Hits: 403  Misses: 14  Evictions: 0  Overflows: 0  Memory Usage: 2kB
--                           ->  Index Scan using customer_pkey on customer c  (cost=0.29..0.31 rows=1 width=17) (actual time=0.003..0.003 rows=1 loops=14)
--                                 Index Cond: (customer_id = rent.customer_id)
-- Planning Time: 0.266 ms
-- Execution Time: 128.746 ms

-- WITH INDEXES
--
-- Limit  (cost=31.67..41.64 rows=10 width=30) (actual time=0.295..1.565 rows=10 loops=1)
--   ->  GroupAggregate  (cost=31.67..159508.26 rows=160000 width=30) (actual time=0.294..1.560 rows=10 loops=1)
-- "        Group Key: car.number, c.first_name, c.second_name"
--         ->  Incremental Sort  (cost=31.67..156308.26 rows=160000 width=22) (actual time=0.161..1.478 rows=321 loops=1)
-- "              Sort Key: car.number, c.first_name, c.second_name"
--               Presorted Key: car.number
--               Full-sort Groups: 8  Sort Method: quicksort  Average Memory: 27kB  Peak Memory: 27kB
--               Pre-sorted Groups: 1  Sort Method: quicksort  Average Memory: 32kB  Peak Memory: 32kB
--               ->  Nested Loop  (cost=0.88..147307.28 rows=160000 width=22) (actual time=0.027..1.236 rows=417 loops=1)
--                     ->  Nested Loop  (cost=0.59..142996.29 rows=160000 width=13) (actual time=0.018..0.984 rows=417 loops=1)
--                           ->  Index Scan using car_number_idx on car  (cost=0.29..4128.29 rows=80000 width=13) (actual time=0.011..0.241 rows=273 loops=1)
--                           ->  Index Scan using rent_car_id_idx on rent  (cost=0.29..1.24 rows=50 width=8) (actual time=0.001..0.002 rows=2 loops=273)
--                                 Index Cond: (car_id = car.car_id)
--                     ->  Memoize  (cost=0.30..0.32 rows=1 width=17) (actual time=0.000..0.000 rows=1 loops=417)
--                           Cache Key: rent.customer_id
--                           Cache Mode: logical
--                           Hits: 403  Misses: 14  Evictions: 0  Overflows: 0  Memory Usage: 2kB
--                           ->  Index Scan using customer_pkey on customer c  (cost=0.29..0.31 rows=1 width=17) (actual time=0.003..0.003 rows=1 loops=14)
--                                 Index Cond: (customer_id = rent.customer_id)
-- Planning Time: 0.363 ms
-- Execution Time: 1.619 ms


-- Displays cars that have never been rented

EXPLAIN ANALYSE
SELECT car.number
FROM car
    LEFT JOIN rent
        ON rent.car_id = car.car_id
    WHERE rent.car_id IS NULL
ORDER BY car.number;

CREATE INDEX second_name_idx ON customer(second_name);
CREATE INDEX car_number_idx ON car(number);
CREATE INDEX rent_customer_id_idx ON rent USING HASH(customer_id);


-- WITHOUT INDEXES
-- Sort  (cost=2375.19..2417.25 rows=16826 width=9) (actual time=48.353..51.826 rows=16826 loops=1)
--   Sort Key: car.number
--   Sort Method: quicksort  Memory: 1557kB
--   ->  Hash Anti Join  (cost=598.00..1194.14 rows=16826 width=9) (actual time=7.801..17.508 rows=16826 loops=1)
--         Hash Cond: (car.car_id = rent.car_id)
--         ->  Seq Scan on car  (cost=0.00..348.00 rows=20000 width=13) (actual time=0.007..1.838 rows=20000 loops=1)
--         ->  Hash  (cost=348.00..348.00 rows=20000 width=4) (actual time=7.758..7.761 rows=20000 loops=1)
--               Buckets: 32768  Batches: 1  Memory Usage: 960kB
--               ->  Seq Scan on rent  (cost=0.00..348.00 rows=20000 width=4) (actual time=0.005..3.119 rows=20000 loops=1)
-- Planning Time: 0.322 ms
-- Execution Time: 52.623 ms
--

-- WITH INDEXES
-- Nested Loop Anti Join  (cost=0.29..1686.46 rows=16826 width=9) (actual time=0.058..38.989 rows=16826 loops=1)
--   ->  Index Scan using car_number_idx on car  (cost=0.29..1044.29 rows=20000 width=13) (actual time=0.033..14.647 rows=20000 loops=1)
--   ->  Index Scan using rent_car_id_idx on rent  (cost=0.00..0.16 rows=6 width=4) (actual time=0.001..0.001 rows=0 loops=20000)
--         Index Cond: (car_id = car.car_id)
-- Planning Time: 0.621 ms
-- Execution Time: 39.846 ms


-- Displays the branch, car model name and the maximum cost of renting a car in it

EXPLAIN ANALYZE
SELECT c.branch_id, branch.branch_name, cm.model, MAX(price) as max_car_price
FROM branch
    INNER JOIN car c
        ON branch.branch_id = c.branch_id
    INNER JOIN car_model cm on c.car_model_id = cm.car_model_id
GROUP BY c.branch_id, branch.branch_name, cm.model
-- the situation with sorting is similar to the first function
-- ORDER BY MAX(price) DESC
LIMIT 5000;

CREATE INDEX car_car_model_id_idx ON car USING HASH(car_model_id);
CREATE INDEX car_branch_id_idx ON car USING HASH(branch_id);
CREATE INDEX car_model_model_idx ON car_model(model);
CREATE INDEX branch_name_idx ON branch(branch_name);
CREATE INDEX price_idx ON car(price);

DROP INDEX IF EXISTS branch_name_idx;
DROP INDEX IF EXISTS price_idx;
DROP INDEX IF EXISTS car_car_model_id_idx;
DROP INDEX IF EXISTS car_branch_id_idx;
DROP INDEX IF EXISTS car_model_model_idx;


-- WITHOUT INDEXES
--
-- Limit  (cost=7904.82..8402.26 rows=5000 width=79) (actual time=43.826..127.752 rows=4991 loops=1)
--   ->  GroupAggregate  (cost=7904.82..15863.94 rows=80000 width=79) (actual time=43.824..127.466 rows=4991 loops=1)
-- "        Group Key: c.branch_id, branch.branch_name, cm.model"
--         ->  Incremental Sort  (cost=7904.82..14263.94 rows=80000 width=52) (actual time=43.814..110.929 rows=80000 loops=1)
-- "              Sort Key: c.branch_id, branch.branch_name, cm.model"
--               Presorted Key: c.branch_id
--               Full-sort Groups: 1979  Sort Method: quicksort  Average Memory: 29kB  Peak Memory: 29kB
--               Pre-sorted Groups: 87  Sort Method: quicksort  Average Memory: 27kB  Peak Memory: 27kB
--               ->  Nested Loop  (cost=7904.71..11412.96 rows=80000 width=52) (actual time=43.776..86.969 rows=80000 loops=1)
--                     ->  Merge Join  (cost=7904.41..9294.28 rows=80000 width=46) (actual time=43.751..61.964 rows=80000 loops=1)
--                           Merge Cond: (branch.branch_id = c.branch_id)
--                           ->  Index Scan using branch_pkey on branch  (cost=0.29..1425.29 rows=40000 width=37) (actual time=0.007..0.942 rows=4999 loops=1)
--                           ->  Sort  (cost=7904.08..8104.08 rows=80000 width=13) (actual time=43.737..50.024 rows=80000 loops=1)
--                                 Sort Key: c.branch_id
--                                 Sort Method: external sort  Disk: 2352kB
--                                 ->  Seq Scan on car c  (cost=0.00..1389.00 rows=80000 width=13) (actual time=0.007..11.438 rows=80000 loops=1)
--                     ->  Memoize  (cost=0.30..0.33 rows=1 width=14) (actual time=0.000..0.000 rows=1 loops=80000)
--                           Cache Key: c.car_model_id
--                           Cache Mode: logical
--                           Hits: 79625  Misses: 375  Evictions: 0  Overflows: 0  Memory Usage: 43kB
--                           ->  Index Scan using car_model_pkey on car_model cm  (cost=0.29..0.32 rows=1 width=14) (actual time=0.001..0.001 rows=1 loops=375)
--                                 Index Cond: (car_model_id = c.car_model_id)
-- Planning Time: 0.215 ms
-- Execution Time: 128.475 ms

-- WITH INDEXES
--
-- Limit  (cost=1.50..2496.09 rows=5000 width=79) (actual time=0.169..137.137 rows=4991 loops=1)
--   ->  GroupAggregate  (cost=1.50..39914.96 rows=80000 width=79) (actual time=0.168..136.855 rows=4991 loops=1)
-- "        Group Key: c.branch_id, branch.branch_name, cm.model"
--         ->  Incremental Sort  (cost=1.50..38314.96 rows=80000 width=52) (actual time=0.152..120.423 rows=80000 loops=1)
-- "              Sort Key: c.branch_id, branch.branch_name, cm.model"
--               Presorted Key: c.branch_id
--               Full-sort Groups: 1979  Sort Method: quicksort  Average Memory: 29kB  Peak Memory: 29kB
--               Pre-sorted Groups: 87  Sort Method: quicksort  Average Memory: 27kB  Peak Memory: 27kB
--               ->  Nested Loop  (cost=0.59..35463.98 rows=80000 width=52) (actual time=0.034..96.264 rows=80000 loops=1)
--                     ->  Nested Loop  (cost=0.29..33345.29 rows=80000 width=46) (actual time=0.022..70.674 rows=80000 loops=1)
--                           ->  Index Scan using branch_pkey on branch  (cost=0.29..1425.29 rows=40000 width=37) (actual time=0.011..4.858 rows=40000 loops=1)
--                           ->  Index Scan using car_branch_id_idx on car c  (cost=0.00..0.55 rows=25 width=13) (actual time=0.000..0.001 rows=2 loops=40000)
--                                 Index Cond: (branch_id = branch.branch_id)
--                     ->  Memoize  (cost=0.30..0.33 rows=1 width=14) (actual time=0.000..0.000 rows=1 loops=80000)
--                           Cache Key: c.car_model_id
--                           Cache Mode: logical
--                           Hits: 79625  Misses: 375  Evictions: 0  Overflows: 0  Memory Usage: 43kB
--                           ->  Index Scan using car_model_pkey on car_model cm  (cost=0.29..0.32 rows=1 width=14) (actual time=0.002..0.002 rows=1 loops=375)
--                                 Index Cond: (car_model_id = c.car_model_id)
-- Planning Time: 0.441 ms
-- Execution Time: 137.353 ms


-- Displays 10 total number of rentals by car in descending order

EXPLAIN ANALYZE
SELECT car.number, COUNT(*) as rent_count
FROM rent
    INNER JOIN car
        ON rent.car_id = car.car_id
    INNER JOIN customer c
        ON rent.customer_id = c.customer_id
GROUP BY car.number
-- the situation with sorting is similar to the first function
-- ORDER BY COUNT(*) DESC
LIMIT 10;


-- WITHOUT INDEXES
--
-- Limit  (cost=8110.57..8111.87 rows=10 width=17) (actual time=87.858..89.605 rows=10 loops=1)
--   ->  Finalize GroupAggregate  (cost=8110.57..8760.96 rows=5003 width=17) (actual time=87.857..89.603 rows=10 loops=1)
--         Group Key: car.number
--         ->  Gather Merge  (cost=8110.57..8685.91 rows=5003 width=17) (actual time=87.846..89.590 rows=21 loops=1)
--               Workers Planned: 1
--               Workers Launched: 1
--               ->  Sort  (cost=7110.56..7123.06 rows=5003 width=17) (actual time=85.161..85.177 rows=344 loops=2)
--                     Sort Key: car.number
--                     Sort Method: quicksort  Memory: 344kB
--                     Worker 0:  Sort Method: quicksort  Memory: 344kB
--                     ->  Partial HashAggregate  (cost=6753.13..6803.16 rows=5003 width=17) (actual time=81.867..82.219 rows=3174 loops=2)
--                           Group Key: car.number
--                           Batches: 1  Memory Usage: 465kB
--                           Worker 0:  Batches: 1  Memory Usage: 465kB
--                           ->  Hash Join  (cost=948.30..6282.54 rows=94118 width=16) (actual time=13.181..67.008 rows=80000 loops=2)
--                                 Hash Cond: (rent.customer_id = c.customer_id)
--                                 ->  Nested Loop  (cost=0.30..5087.45 rows=94118 width=13) (actual time=0.036..37.253 rows=80000 loops=2)
--                                       ->  Parallel Seq Scan on rent  (cost=0.00..2118.18 rows=94118 width=8) (actual time=0.007..4.533 rows=80000 loops=2)
--                                       ->  Memoize  (cost=0.30..0.34 rows=1 width=13) (actual time=0.000..0.000 rows=1 loops=160000)
--                                             Cache Key: rent.car_id
--                                             Cache Mode: logical
--                                             Hits: 83594  Misses: 3174  Evictions: 0  Overflows: 0  Memory Usage: 360kB
--                                             Worker 0:  Hits: 70058  Misses: 3174  Evictions: 0  Overflows: 0  Memory Usage: 360kB
--                                             ->  Index Scan using car_pkey on car  (cost=0.29..0.33 rows=1 width=13) (actual time=0.001..0.001 rows=1 loops=6348)
--                                                   Index Cond: (car_id = rent.car_id)
--                                 ->  Hash  (cost=548.00..548.00 rows=32000 width=11) (actual time=13.061..13.062 rows=32000 loops=2)
--                                       Buckets: 32768  Batches: 1  Memory Usage: 1650kB
--                                       ->  Seq Scan on customer c  (cost=0.00..548.00 rows=32000 width=11) (actual time=0.020..5.390 rows=32000 loops=2)
-- Planning Time: 0.503 ms
-- Execution Time: 89.703 ms

-- WITH INDEXES
--
-- Limit  (cost=0.59..253.97 rows=10 width=17) (actual time=0.211..1.574 rows=10 loops=1)
--   ->  GroupAggregate  (cost=0.59..126765.31 rows=5003 width=17) (actual time=0.210..1.571 rows=10 loops=1)
--         Group Key: car.number
--         ->  Nested Loop  (cost=0.59..125915.28 rows=160000 width=16) (actual time=0.093..1.501 rows=545 loops=1)
--               ->  Nested Loop  (cost=0.29..121604.29 rows=160000 width=13) (actual time=0.077..1.249 rows=545 loops=1)
--                     ->  Index Scan using car_number_idx on car  (cost=0.29..3904.29 rows=80000 width=13) (actual time=0.009..0.228 rows=305 loops=1)
--                     ->  Index Scan using rent_car_id_idx on rent  (cost=0.00..0.97 rows=50 width=8) (actual time=0.002..0.003 rows=2 loops=305)
--                           Index Cond: (car_id = car.car_id)
--               ->  Memoize  (cost=0.30..0.32 rows=1 width=11) (actual time=0.000..0.000 rows=1 loops=545)
--                     Cache Key: rent.customer_id
--                     Cache Mode: logical
--                     Hits: 527  Misses: 18  Evictions: 0  Overflows: 0  Memory Usage: 2kB
--                     ->  Index Scan using customer_pkey on customer c  (cost=0.29..0.31 rows=1 width=11) (actual time=0.003..0.003 rows=1 loops=18)
--                           Index Cond: (customer_id = rent.customer_id)
-- Planning Time: 0.225 ms
-- Execution Time: 1.618 ms

ROLLBACK;
END;