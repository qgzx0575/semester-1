.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- SELECT name FROM drivers; -- names
-- SELECT name FROM menu_items WHERE price>10; -- items over £10
-- SELECT postcode FROM restaurants WHERE postcode LIKE 'LS2%'; -- sort for starting with LS2
/*
postcode
--------
LS2 9JT
LS2 7EJ
LS2 8BQ
LS2 7HU
LS2 3AA
LS2 9HD
*/
-- SELECT name FROM restaurants ORDER BY name LIMIT 3 WHERE cuisine = 'Thai'; -- Error: WHERE should come before ORDER BY and LIMIT
-- "What is the degree of a relation with attributes (columns): id, name and email?" -- 3