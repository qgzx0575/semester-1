.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.
-- A
SELECT name FROM restaurants
WHERE hygiene_rating = 5;
/*
Bella Napoli       
Bangkok Garden     
Seoul Kitchen      
Taqueria Azul      
Cedar Tree         
Sakura House       
Olive and Feta     
Dosa Corner        
Jerk Shack         
Saigon Kitchen     
Smokehouse Kitchen
*/
-- B
SELECT name FROM restaurants
WHERE postcode LIKE 'LS6%';
/*
Bella Napoli    
Bangkok Garden  
Taqueria Azul   
Cedar Tree      
Olive and Feta  
Tandoori Nights 
Kimchi Street   
Saigon Kitchen
*/
-- C
SELECT name FROM restaurants
WHERE cuisine = 'italian';
/* 
No output, because WHERE is case-sensitive
*/
-- D
SELECT name FROM restaurants
WHERE cuisine = 'Italian' OR
cuisine = 'Thai' AND hygiene_rating = 5;
/*
Bella Napoli   
Bangkok Garden 
Pasta Pronto   
Trattoria Roma 
Pizza Forno
*/