-- triggers


CREATE OR REPLACE FUNCTION check_phone_number()
-- Checks if the phone number is correct
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
IF NEW.phone_number NOT LIKE '09________' THEN
-- 	    RAISE EXCEPTION 'Invalid phone_number format!';
    RAISE NOTICE 'Invalid phone_number format!';
    RETURN NULL;
END IF;

RETURN NEW;
END;
$$;

CREATE TRIGGER before_update_insert_phone_number
  BEFORE UPDATE OR INSERT
  ON phone_number
  FOR EACH ROW
  EXECUTE PROCEDURE check_phone_number();

INSERT INTO phone_number (phone_number) VALUES ('0952014752'), ('0935674875');
INSERT INTO phone_number (phone_number) VALUES ('0952014752'), ('0934875');
INSERT INTO phone_number (phone_number) VALUES ('095201472'), ('093564875');
UPDATE phone_number SET phone_number = '0952014752' WHERE phone_number_id = 500;
UPDATE phone_number SET phone_number = '092014752' WHERE phone_number_id = 500;

CREATE OR REPLACE FUNCTION price_maximum_comparison()
-- Checks that the price does not exceed the maximum allowable
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
    DECLARE
        max_price_arg decimal;
BEGIN

max_price_arg = TG_ARGV[0];
IF NEW.price > max_price_arg
THEN
    UPDATE car
    SET price = max_price_arg
    WHERE car_id = NEW.car_id;
END IF;

RETURN NEW;
END;
$$;

CREATE TRIGGER before_update_insert_phone_number
  AFTER UPDATE OR INSERT
  ON car
  FOR EACH ROW
  EXECUTE PROCEDURE price_maximum_comparison(10000);

DROP TRIGGER before_update_insert_phone_number ON car;


INSERT INTO car (branch_id, car_model_id, number, price) VALUES (500, 80, '85423684', 5000);
INSERT INTO car (branch_id, car_model_id, number, price) VALUES (500, 80, '85423684', 25000);
UPDATE car SET price = 4000 WHERE car_id = 700;
UPDATE car SET price = 85000 WHERE car_id = 700;
