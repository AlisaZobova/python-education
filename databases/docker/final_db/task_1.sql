-- Creating a database, creating tables, adding links between tables, filling the table with data


-- sudo docker-compose --env-file ./.env.list exec db psql -U postgres -c "CREATE DATABASE car_rental;"

CREATE TABLE IF NOT EXISTS car_brand(
    car_brand_id SERIAL PRIMARY KEY,
    brand VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS car_model(
    car_model_id SERIAL PRIMARY KEY,
    car_brand_id INT NOT NULL,
    model VARCHAR(50),
    CONSTRAINT fk_car_brand_id
        FOREIGN KEY(car_brand_id)
            REFERENCES car_brand(car_brand_id)
);

CREATE TABLE IF NOT EXISTS city(
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS street(
    street_id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    street_name VARCHAR(50),
    CONSTRAINT fk_city_id
        FOREIGN KEY(city_id)
            REFERENCES city(city_id)
);

CREATE TABLE IF NOT EXISTS house(
    house_id SERIAL PRIMARY KEY,
    street_id INT NOT NULL,
    num VARCHAR (5),
    CONSTRAINT fk_street_id
        FOREIGN KEY(street_id)
            REFERENCES street(street_id)
);

CREATE TABLE IF NOT EXISTS phone_number(
    phone_number_id SERIAL PRIMARY KEY,
    phone_number VARCHAR (20)
);

CREATE TABLE IF NOT EXISTS branch(
    branch_id SERIAL PRIMARY KEY,
    house_id INT NOT NULL,
    phone_number_id INT NOT NULL,
    branch_name VARCHAR (50),
    CONSTRAINT fk_house_id
        FOREIGN KEY(house_id)
            REFERENCES house(house_id),
    CONSTRAINT fk_phone_number_id
        FOREIGN KEY(phone_number_id)
            REFERENCES phone_number(phone_number_id)
);

CREATE TABLE IF NOT EXISTS car(
    car_id SERIAL PRIMARY KEY,
    branch_id INT NOT NULL,
    car_model_id INT NOT NULL,
    number VARCHAR(50),
    price DECIMAL(10, 2),
    CONSTRAINT fk_branch_id
        FOREIGN KEY(branch_id)
            REFERENCES branch(branch_id),
    CONSTRAINT fk_car_model_id
        FOREIGN KEY(car_model_id)
            REFERENCES car_model(car_model_id)
);

CREATE TABLE IF NOT EXISTS customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50),
    second_name VARCHAR (50),
    house_id INT NOT NULL,
    phone_number_id INT NOT NULL,
    CONSTRAINT fk_house_id
        FOREIGN KEY(house_id)
            REFERENCES house(house_id),
    CONSTRAINT fk_phone_number_id
        FOREIGN KEY(phone_number_id)
            REFERENCES phone_number(phone_number_id)
);

CREATE TABLE IF NOT EXISTS rent(
    rent_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    car_id INT NOT NULL,
    date_of_renting DATE NOT NULL,
    period_of_renting INTERVAL,
    CONSTRAINT fk_customer_id
        FOREIGN KEY(customer_id)
            REFERENCES customer(customer_id),
    CONSTRAINT fk_car_id
        FOREIGN KEY(car_id)
            REFERENCES car(car_id)
);

CREATE OR REPLACE PROCEDURE insert_into_car_brand(
brands VARCHAR ARRAY
)
LANGUAGE plpgsql
AS $$
DECLARE
    brand_name VARCHAR;
BEGIN
    FOR i IN 1..100
    LOOP
    FOREACH brand_name IN ARRAY brands
        LOOP
        INSERT INTO car_brand (brand) VALUES (brand_name || ' ' || i);
        END LOOP;
    END LOOP;
END;$$;

CALL insert_into_car_brand(
    ARRAY [
    'Aston Martin Lagonda Ltd',
    'BMW',
    'Chevrolet',
    'Dodge',
    'Ferrari',
    'Honda',
    'Jaguar',
    'Lamborghini',
    'MAZDA',
    'McLaren',
    'Mercedes-Benz',
    'NISSAN',
    'Pagani Automobili S.p.A.',
    'Porsche',
    'FIAT',
    'Mini',
    'SCION',
    'Subaru',
    'Bentley',
    'Buick',
    'Ford',
    'HYUNDAI MOTOR COMPANY',
    'LEXUS',
    'MASERATI',
    'Roush',
    'Volkswagen',
    'Acura',
    'Cadillac',
    'INFINITI',
    'KIA MOTORS CORPORATION',
    'Mitsubishi Motors Corporation',
    'Rolls-Royce Motor Cars Limited',
    'TOYOTA',
    'Volvo',
    'Chrysler',
    'Lincoln',
    'GMC',
    'RAM',
    'CHEVROLET',
    'Jeep',
    'Land Rover']);

-- sudo docker cp ./final_db/car_models.csv docker-db-1:/usr/src/car_models.csv

COPY car_model(car_brand_id, model)
FROM '/usr/src/car_models.csv'
DELIMITER ',';

-- sudo docker cp ./final_db/uscities.csv docker-db-1:/usr/src/uscities.csv

COPY city(city_name)
FROM '/usr/src/uscities.csv'
DELIMITER ',';

-- sudo docker cp ./final_db/streets.csv docker-db-1:/usr/src/streets.csv

COPY street(city_id, street_name)
FROM '/usr/src/streets.csv'
DELIMITER ',';

CREATE OR REPLACE FUNCTION random_between(low INT, high INT)
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$ language plpgsql STRICT;

INSERT INTO house(street_id, num)
SELECT random_between(1, 2040), random_between(1, 9999)
FROM generate_series(1, 5000);

INSERT INTO phone_number(phone_number)
SELECT '09' || random_between(10000000, 99999999)
FROM generate_series(1, 5000);

INSERT INTO branch(house_id, phone_number_id, branch_name)
SELECT random_between(1, 5000), random_between(1, 5000), md5(random()::text)
FROM generate_series(1, 5000);

INSERT INTO car(car_model_id, branch_id, number, price)
SELECT random_between(1, 375),
       random_between(1, 5000),
       random_between(10000000, 99999999),
       random_between(10, 9999) :: DECIMAL
FROM generate_series(1, 5000);

-- sudo docker cp ./final_db/names.csv docker-db-1:/usr/src/names.csv
COPY customer(first_name, second_name, house_id, phone_number_id)
FROM '/usr/src/names.csv'
DELIMITER ',';

INSERT INTO rent(customer_id, car_id, date_of_renting, period_of_renting)
SELECT
random_between(1, 1000),
random_between(1, 5000),
timestamp '2022-01-10 20:00:00' +
random() * (timestamp '2022-05-20 20:00:00' -
timestamp '2022-01-10 10:00:00'),
trunc(random()  * 20) * '1 day'::interval
FROM
generate_series(1, 5000);
