.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- YOU SHOULD RUN ANY 'UPDATES' AS SELECTS FIRST - it's very easy to accidentally update more than you intended..

-- SELECT * FROM restaurants WHERE cuisine != UPPER(cuisine);
-- UPDATE restaurants SET cuisine = UPPER(cuisine); -- updated to be capitalized

-- SELECT * FROM restaurants WHERE postcode != UPPER(postcode);
-- UPDATE restaurants SET postcode = UPPER(postcode); -- updated to be capitalized

-- SELECT * FROM orders WHERE delivery_fee IS NULL;
-- UPDATE orders SET delivery_fee = 2.49 WHERE delivery_fee IS NULL; -- updated delivery_fee to 2.49 where it was NULL

-- SELECT * FROM customers WHERE email LIKE '%@test.com';
-- DELETE FROM customers WHERE email LIKE '%@test.com'; -- delete customers with test emails

-- SELECT name, COUNT(*) as count FROM restaurants WHERE name LIKE name GROUP BY name HAVING count > 1; -- locate duplicate restaurants by name
-- DELETE FROM restaurants WHERE restaurant_id = 99; -- delete duplicate restaurant 