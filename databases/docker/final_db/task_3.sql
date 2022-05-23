-- views


-- Shows how many cars of certain brands are on each of the branches

CREATE MATERIALIZED VIEW car_count_on_branch_by_brand AS
SELECT branch_name, brand, COUNT(branch) AS car_brand_count
FROM branch
    INNER JOIN car c
        on branch.branch_id = c.branch_id
    INNER JOIN car_model cm
        on c.car_model_id = cm.car_model_id
    INNER JOIN car_brand cb
        on cb.car_brand_id = cm.car_brand_id
GROUP BY branch_name, brand
ORDER BY COUNT(branch) DESC, branch_name;

SELECT * FROM car_count_on_branch_by_brand;

-- Calculates profit for March by branches

CREATE OR REPLACE VIEW march_profit AS
SELECT branch_name, SUM(extract(DAY FROM period_of_renting) * price) as profit
FROM branch INNER JOIN car c on branch.branch_id = c.branch_id FULL JOIN rent r on c.car_id = r.car_id
WHERE date_of_renting BETWEEN '2022-03-01' AND '2022-03-31'
GROUP BY branch_name
ORDER BY SUM(extract(DAY FROM period_of_renting) * price) DESC;

SELECT * FROM march_profit;

-- Shows which branches have bmw cars

CREATE OR REPLACE VIEW bmw_branch
AS
SELECT branch_name
FROM branch
    INNER JOIN car c
        on branch.branch_id = c.branch_id
    INNER JOIN car_model cm
        on cm.car_model_id = c.car_model_id
    INNER JOIN car_brand cb
        on cb.car_brand_id = cm.car_brand_id
WHERE cb.brand LIKE 'BMW%';

SELECT * FROM bmw_branch;
