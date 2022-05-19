-- TASK 1

CREATE OR REPLACE VIEW user_order AS
SELECT users.city AS city, o.order_id as order_id, o.shipping_total AS sh_total
FROM users
INNER JOIN carts c
    ON users.user_id = c.users_user_id
INNER JOIN _order o
    ON c.cart_id = o.carts_cart_id;

DROP VIEW user_order;

SELECT SUM(shipping_total)
FROM _order;

-- 90000

CREATE OR REPLACE FUNCTION set_shipping_total(x VARCHAR(100))
RETURNS DECIMAL
LANGUAGE plpgsql
AS $$
DECLARE
    sum_total DECIMAL;
    us_ord RECORD;
BEGIN
    FOR us_ord IN (SELECT * FROM user_order)
    LOOP
        IF us_ord.city = x
            THEN
                UPDATE _order
                SET shipping_total = 0
                WHERE order_id = us_ord.order_id;
            END IF;
        END LOOP;

    SELECT SUM(shipping_total)
    INTO sum_total
    FROM _order;
    RETURN sum_total;
END;$$;

SELECT set_shipping_total('city 5') AS order_sum;

-- 89940

-- TASK 2

-- Procedure that checks if the customer has enough money to pay for the order
-- and what is the status of the order (whether it needs payment)

CREATE OR REPLACE PROCEDURE payment(
   o_id INT,
   money DECIMAL
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF o_id IN (SELECT order_id FROM _order WHERE order_status_order_status_id IN (1, 2))
    THEN
    IF money >= (SELECT total FROM _order WHERE order_id = o_id)
        THEN
        UPDATE _order
        SET order_status_order_status_id = 3
        WHERE order_id = o_id;
        RAISE NOTICE 'PAYMENT WAS SUCCESSFUL :)';
        COMMIT;
    ELSE
        RAISE NOTICE 'NO ENOUGH MONEY TO PAY FOR THE ORDER!';
    END IF;
    ELSE
        RAISE NOTICE 'ORDER HAS BEEN PAID, FINISHED OR CANCELED!';
    END IF;
END;$$;

CALL payment(45, 5);
CALL payment(46, 1000);
CALL payment(49, 840);


-- Checks if an overlimit has occurred at the cash register,
-- if the next payment will lead to an overlimit, stops payments

CREATE OR REPLACE PROCEDURE overlimit(
   o_id int[],
   max_limit DECIMAL
)
LANGUAGE plpgsql
AS $$
DECLARE
    limit_condition DECIMAL;
    id INT;
BEGIN
    FOREACH id in ARRAY o_id
    LOOP
        limit_condition := max_limit - (SELECT total FROM _order WHERE order_id = id);

        IF limit_condition >= 0 THEN
            max_limit := limit_condition;
        ELSE
            RAISE NOTICE 'AT THE CASH OFFICE IS OVERLIMITED, PLEASE WAIT WITH PAYMENT OF ORDERS, STARTING WITH ID %!', id;
            EXIT;

        END IF;
        END LOOP;

    IF limit_condition >= 0 THEN
        RAISE NOTICE 'ALL PAYMENTS PASSED SUCCESSFULLY!';

    END IF;
END;$$;

CALL overlimit(array [191, 1013, 750, 45], 3000);
CALL overlimit(array [191, 1013], 3000);


-- Checks if there are enough products that want to be added to the cart in stock,
-- if enough - reduces the number of products left in stock, updates the amount in the cart,
-- adds a cart-product relationship and increases the total amount of the order

CREATE OR REPLACE PROCEDURE add_product_to_cart(
    c_id int,
    prod_title VARCHAR(100),
    amount int
)
LANGUAGE plpgsql
AS $$
DECLARE
    new_sum DECIMAl;
    cart record;
    product record;
BEGIN
    IF c_id IN (SELECT cart_id FROM carts)
        THEN
        SELECT product_id, in_stock, price
        INTO product
        FROM products WHERE product_title = prod_title;

        SELECT cart_id, total
        INTO cart
        FROM carts WHERE cart_id = c_id;

    IF product.in_stock >= amount
        THEN
        UPDATE products
        SET in_stock = in_stock - amount
        WHERE product_title = prod_title;

        new_sum = cart.total + amount * product.price;

        UPDATE carts
        SET subtotal = new_sum, total = new_sum, _timestamp = now()
        WHERE cart_id = c_id;

        INSERT INTO cart_product (carts_cart_id, products_product_id)
        VALUES (cart.cart_id, product.product_id);

        UPDATE _order
        SET total = new_sum, updated_at = now()
        WHERE carts_cart_id = cart.cart_id;

        RAISE NOTICE 'PRODUCT HAS BEEN SUCCESSFULLY ADDED :)';
        COMMIT;
    ELSE
        RAISE NOTICE 'NOT ENOUGH PRODUCTS IN STOCK!';
    END IF;
    ELSE
        RAISE NOTICE 'THERE IS NO SUCH CART!';
    END IF;
END;$$;

CALL add_product_to_cart(1, 'Product 7', 7);
CALL add_product_to_cart(5000, 'Product 2', 1);
CALL add_product_to_cart(500, 'Product 2', 1);
