.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- No. 1
-- SELECT * FROM drivers;
/* 
driver_id      name       vehicle     phone
---------  -------------  -------  ------------
        1  Priya Shah     scooter  07700 900928
        2  Joel Xu        scooter  07700 900915
        3  Hamza O'Brien  scooter  07700 900313
        4  Jade Park      scooter  07700 900064
        5  Nadia Varga    bike     07700 900933
        6  Leah Shah      car      07700 900168
        7  Xin Wright     car      07700 900127
        8  Xin Patel      car      07700 900061
        9  Lucy Ali       car      07700 900654
       10  Jack Garcia    car      07700 900944
       11  Deepa Jones    scooter  07700 900334
       12  Harry Shah     bike     07700 900917
       13  Uma Singh      bike     07700 900785
       14  Uma Wilson     car      07700 900619
       15  Niamh Khan     bike     07700 900929
       16  Zara Mensah    car      07700 900935
       17  Kiran Walker   e-bike   07700 900715
       18  Zain Patel     e-bike   07700 900546
*/

-- No. 2
-- SELECT name, price FROM menu_items WHERE restaurant_id = 3;
/*
         name           price
----------------------  -----
Red curry with prawns     9.5
Massaman beef curry       7.5
Basil chicken             8.5
Tom yum soup              7.5
Vegetable spring rolls    5.5
Pad see ew              11.95
Pad Thai with chicken    9.95
Papaya salad            10.95
Green curry with tofu   11.95
*/

-- No. 5
-- SELECT name, price FROM menu_items WHERE price<=8 AND is_vegetarian=1 ORDER BY price ASC;
/* 
         name           price
----------------------  -----
Egg fried rice            3.5
Hot and sour soup         3.5
Baba ganoush              3.5
Edamame                   3.5
Callaloo                  3.5
Tzatziki and pitta        3.5
Onion rings               3.5
Garlic bread              3.5
Rice and peas             3.5
Festival dumplings        3.5
Tzatziki and pitta        3.5
Guacamole and chips      3.95
Loaded fries             3.95
Onion bhaji              3.95
Edamame                  3.95
Garlic naan              3.95
Onion bhaji              3.95
Nachos                    4.0
Hummus and pitta          4.0
Summer rolls              4.0
Egg fried rice            4.0
Summer rolls              4.0
Lentil soup               4.0
Onion rings               4.0
Garlic bread              4.5
Lentil soup               4.5
Garlic naan               4.5
Hot and sour soup         4.5
Fried plantain            4.5
Tabbouleh                 4.5
Hummus and pitta          4.5
Guacamole and chips       4.5
Loukoumades               4.5
Garlic bread              4.5
Garlic naan              4.95
Vegetable dumplings      4.95
Tabbouleh                4.95
Baklava                  4.95
Rice and peas            4.95
Loukoumades              4.95
Baklava                  4.95
Baba ganoush             4.95
Sticky rice with mango   4.95
Nachos                   4.95
Onion bhaji               5.5
Vegetable spring rolls    5.5
Churros                   5.5
Brownie sundae            5.5
Loaded fries              5.5
Tiramisu                 5.95
Churros                  5.95
Tiramisu                 5.95
Tiramisu                  6.5
Halloumi wrap             6.5
Halloumi plate            6.5
Kunefe                    6.5
Brownie sundae            6.5
Mushroom risotto          6.5
Japchae                   6.5
Quesadilla                6.5
Mushroom risotto         6.95
Chana masala             6.95
Kimchi fried rice        6.95
Greek salad              6.95
Halloumi souvlaki        6.95
Caprese salad            6.95
Vegetable patty          6.95
Mushroom risotto         6.95
Masala dosa               7.5
Falafel plate             7.5
Tteokbokki                7.5
Falafel plate             7.5
Mixed meze               7.95
Penne arrabbiata         7.95
Vegetable biryani        7.95
*/

-- No. 6
-- SELECT name, hygiene_rating FROM restaurants WHERE hygiene_rating < 4 ORDER BY hygiene_rating ASC;
/*
        name          hygiene_rating
--------------------  --------------
Brooklyn Burger Co                 2
Thai Orchid                        2
Pasta Pronto                       3
Anatolia Grill                     3
Tandoori Nights                    3
Kimchi Street                      3
Istanbul Kebab House               3
Pizza Forno                        3
*/

-- No. 11
-- SELECT * FROM orders WHERE status = 'placed' AND 2026-10-01 <= order_time < 2026-11-01; -- Ran this first, found out there was no driver id for the stuck orders
/*
order_id  customer_id  restaurant_id  driver_id     order_time     status  delivery_fee
--------  -----------  -------------  ---------  ----------------  ------  ------------
    1812          114              8             2026-10-02 19:05  placed          3.49
    1817           83              9             2026-10-02 21:32  placed          2.99
    1853           97             25             2026-10-05 20:56  placed          2.49
    2010           76              1             2026-10-18 17:23  placed          3.49
    2042          122             23             2026-10-21 18:51  placed          2.99
    2079          118             10             2026-10-24 19:44  placed          2.99
    2281           60             20             2026-11-09 15:15  placed          2.99
    2287           96              3             2026-11-09 19:37  placed           0.0
    2291           73             16             2026-11-10 12:01  placed          2.49
*/
-- SELECT order_id, driver_id, status FROM orders WHERE status = 'placed' AND 2026-10-01 <= order_time < 2026-11-01; -- kept order_id (primary key), driver_id, and status (issues)
/*
order_id  driver_id  status
--------  ---------  ------
    1812             placed
    1817             placed
    1853             placed
    2010             placed
    2042             placed
    2079             placed
    2281             placed
    2287             placed
    2291             placed
*/

-- No. 12
-- SELECT name, price FROM menu_items ORDER BY price LIMIT 5 WHERE is_vegetarian = 1; -- Old query, WHERE comes too late
-- SELECT name, price FROM menu_items WHERE is_vegetarian = 1 ORDER BY price LIMIT 5; -- New query, moved WHERE to after FROM
-- SELECT name, price FROM menu_items WHERE is_vegetarian = 1 LIMIT 5; -- Old query, forgot ORDER BY, resorts to default sorting, which is then truncated
-- SELECT name, price FROM menu_items WHERE is_vegetarian = 1 ORDER BY price LIMIT 5; -- New query, added ORDER BY price

-- No. 13
-- SELECT * FROM menu_items ORDER BY price LIMIT 1; -- Limit of only 1
/*
item_id  restaurant_id       name       price  is_vegetarian
-------  -------------  --------------  -----  -------------
     49              6  Egg fried rice    3.5              1
*/
-- SELECT * FROM menu_items ORDER BY price LIMIT 5; -- Limit of 5; many dishes at the cheapest option, they can choose from multiple
/*
item_id  restaurant_id        name         price  is_vegetarian
-------  -------------  -----------------  -----  -------------
     49              6  Egg fried rice       3.5              1
     50              6  Hot and sour soup    3.5              1
     70              8  Baba ganoush         3.5              1
     90             10  Edamame              3.5              1
     95             11  Callaloo             3.5              1
*/

-- No. 14
-- SELECT * FROM orders WHERE TIME(order_time) >= '21:00' ORDER BY order_time; -- You can tell late night bites occur between 21:00 and 23:00

