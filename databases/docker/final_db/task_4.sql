-- functions


-- Returns a table of prices and numbers of cars of a certain model by branch

create or replace function get_cars_by_model(
  car_model varchar
)
	returns table (
		branch varchar,
		car_number varchar,
		car_price decimal
	)
	language plpgsql
as $$
begin
	return query
		select
			branch_name, number, price
		from branch
            INNER JOIN car c
                ON branch.branch_id = c.branch_id
            INNER JOIN car_model cm
                ON cm.car_model_id = c.car_model_id
		where
			cm.model = car_model;
end;$$;

SELECT * FROM get_cars_by_model('A6');

-- Returns all branches from the given city

create or replace function get_branches_by_city(city varchar)
returns varchar array as $$
declare
    branches varchar array;
    new_branch record;
    cur_branch cursor(city varchar)
     for select branch_name
     from branch
         INNER JOIN house h
             ON h.house_id = branch.house_id
         INNER JOIN street s
             ON s.street_id = h.street_id
         INNER JOIN city c
             ON c.city_id = s.city_id
     WHERE c.city_name = city;
begin
   open cur_branch(city);

   loop
      fetch cur_branch into new_branch;
      branches := array_append(branches, new_branch.branch_name);
      exit when not found;
   end loop;

   close cur_branch;
   return branches;
end; $$
language plpgsql;

SELECT get_branches_by_city('Coal City');

-- Updates the price to a new one with a discount, returns the total discount for the branch

CREATE OR REPLACE FUNCTION set_price_with_discount(branch varchar, discount integer, min_price decimal)
RETURNS DECIMAL
LANGUAGE plpgsql
AS $$
DECLARE
    total_discount decimal;
    sum_prices_before decimal;
    sum_prices_after decimal;
    new_price decimal;
    cur_car record;
BEGIN
    sum_prices_before = (SELECT SUM(price)
                         FROM car
                         INNER JOIN branch b
                             ON b.branch_id = car.branch_id
                         WHERE b.branch_name = branch
                         GROUP BY b.branch_id);

    FOR cur_car IN (SELECT car_id, price
                    FROM car
                        INNER JOIN branch b
                            ON b.branch_id = car.branch_id
                    WHERE b.branch_name = branch)
    LOOP
        new_price = cur_car.price - cur_car.price * discount / 100;
        IF new_price < min_price
            THEN
                new_price = min_price;
            END IF;

        UPDATE car
        SET price = new_price
        WHERE car_id = cur_car.car_id;

    END LOOP;

    sum_prices_after = (SELECT SUM(price)
                        FROM car
                        INNER JOIN branch b
                            ON b.branch_id = car.branch_id
                        WHERE b.branch_name = branch
                        GROUP BY b.branch_id);

    total_discount = sum_prices_before - sum_prices_after;

    RETURN total_discount;

END;$$;

SELECT set_price_with_discount('bd53f14b9bbc38d1543d9e4fbe0819ad', 5, 100);
