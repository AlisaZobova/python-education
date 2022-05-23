-- stored procedures


-- The procedure removes customers who have never rented a car,
-- but the relatives of the branch owners cannot be removed from the table,
-- even if they do not bring profit

CREATE OR REPLACE PROCEDURE removing_useless_users(owner_surnames varchar array)
LANGUAGE plpgsql
AS
$$
DECLARE
    cur_customer record;
BEGIN
    FOR cur_customer IN (
    SELECT customer.customer_id, second_name
    FROM customer
     LEFT JOIN rent r
         on customer.customer_id = r.customer_id
    WHERE r.customer_id IS NULL)

    LOOP
        DELETE FROM customer WHERE customer_id = cur_customer.customer_id;
        IF cur_customer.second_name = ANY (owner_surnames)
            THEN
            ROLLBACK;
        ELSE
            COMMIT;
        end if;
        end loop;
end;
    $$;

CALL removing_useless_users(array ['GRIMES', 'MCMILLAN']);

-- CHECK

SELECT customer.customer_id, second_name
FROM customer
 LEFT JOIN rent r
     on customer.customer_id = r.customer_id
WHERE r.customer_id IS NULL;

-- A view that returns data about the client, car, and rental period, which are specified in the rental record

CREATE OR REPLACE VIEW rent_car_customers AS
SELECT first_name,
       second_name,
       number,
       date_of_renting,
       period_of_renting,
       rent_id,
       c2.customer_id,
       c.car_id
FROM rent
    INNER JOIN car c
        on c.car_id = rent.car_id
    inner join customer c2
        on c2.customer_id = rent.customer_id;

-- The procedure changes the number of rental days if a record with the corresponding data exists,
-- if not, it checks if there is a car with the given number and a person with the corresponding
-- first and last name, and adds a new rental record

CREATE OR REPLACE PROCEDURE update_or_create_rent(name varchar, surname varchar, car_num varchar, rent_date date, period interval)
    LANGUAGE plpgsql
AS
$$
DECLARE
    cur_rent record default NULL;
    cust_id INT default NULL;
    c_id INT DEFAULT NULL;
BEGIN
    SELECT * FROM rent_car_customers
     WHERE first_name = name
       AND second_name = surname
       AND number = car_num
       AND date_of_renting = rent_date
     INTO cur_rent;
    IF cur_rent IS NOT NULL
        THEN
        IF cur_rent.period_of_renting != period
            THEN
                UPDATE rent
                 set period_of_renting = period
                 WHERE rent_id = cur_rent.rent_id;
            end if;
    ELSE
        cust_id = (SELECT customer_id FROM customer WHERE first_name = name AND second_name = surname);
        c_id = (SELECT car_id FROM car WHERE number = car_num);
        IF cust_id IS NOT NULL AND c_id IS NOT NULL
        THEN
            INSERT INTO rent (customer_id, car_id, date_of_renting, period_of_renting)
            VALUES (cust_id, c_id, now(), period);
        ELSE
            RAISE EXCEPTION 'NO SUCH CAR OR CUSTOMER!';
        end if;
    end if;
end;
    $$;

CALL update_or_create_rent('SMITH','THOMAS', '59510719', '25 days'::interval);
CALL update_or_create_rent('SMITH','THOMAS', '90871605', '5 days'::interval);
CALL update_or_create_rent('STH','THOMAS', '90871605', '5 days'::interval);
