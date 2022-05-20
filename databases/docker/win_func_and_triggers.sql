-- TASK 1

SELECT
	category_title,
	product_title,
	price,
	AVG (price) OVER (
	   PARTITION BY category_title
	)
FROM
	products
	INNER JOIN
		categories USING (category_id);

-- TASK 2

CREATE OR REPLACE VIEW cart_order_id AS
    SELECT product_id, cart_id,order_id
	FROM products
	    INNER JOIN cart_product cp
	        ON products.product_id = cp.products_product_id
	    INNER JOIN carts c
	        ON c.cart_id = cp.carts_cart_id
	    INNER JOIN _order o
	        ON c.cart_id = o.carts_cart_id;


CREATE OR REPLACE FUNCTION check_price()
-- Checks if the updated or new cost is greater than 0, updates the entities associated with the price of this product
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
DECLARE
    diff DECIMAL;
    id INT;
BEGIN
	IF NEW.price <= 0 THEN
-- 	    Throwing an exception/returning null rollback the transaction instead of a rollback

-- 	    RAISE EXCEPTION 'The price cannot be negative!';
		RAISE NOTICE 'The price cannot be negative!';
		RETURN NULL;
	END IF;

	diff = NEW.price - OLD.price;
    id = OLD.product_id;

	OLD.price = NEW.price;

	UPDATE carts
	SET subtotal = subtotal + diff,
	    total = total + diff
	WHERE cart_id IN (SELECT cart_id FROM cart_order_id WHERE product_id = id);

	UPDATE _order
	SET total = total + diff
	WHERE order_id IN (SELECT order_id FROM cart_order_id WHERE product_id = id);

	RETURN NEW;
END;
$$;

CREATE TRIGGER before_update_insert_price
  BEFORE UPDATE OR INSERT
  ON products
  FOR EACH ROW
  EXECUTE PROCEDURE check_price();

UPDATE products SET price = 150 WHERE product_id = 1;

INSERT INTO products (product_title, product_description, in_stock, price, slug, category_id)
VALUES ('Product 52525', 'Product description 52525', 38, -197.92, 'Product-52525', 15);

--

CREATE OR REPLACE FUNCTION check_email()
-- Checks if the email is correct
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	IF NEW.email NOT LIKE '%@%.%' THEN
-- 	    Throwing an exception/returning null rollback the transaction instead of a rollback

-- 	    RAISE EXCEPTION 'Invalid email format!';
		RAISE NOTICE 'Invalid email format!';
		RETURN NULL;
	END IF;

	RETURN NEW;
END;
$$;

CREATE TRIGGER before_update_insert_email
  BEFORE UPDATE OR INSERT
  ON users
  FOR EACH ROW
  EXECUTE PROCEDURE check_email();

UPDATE users
SET email = 'hgvgy'
WHERE user_id = 1;

UPDATE users
SET email = 'good_email@gmail.com'
WHERE user_id = 1;
