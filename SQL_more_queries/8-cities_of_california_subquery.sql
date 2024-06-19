-- Script that lists all the cities of California that can be found in the database 'hbtn_0d_usa'

-- Use database 'hbtn_0d_usa'
USE hbtn_0d_usa;
-- Command 'Select' combined to 'Where' and 'Order by'
SELECT name
FROM cities
WHERE state = 'California'
ORDER BY cities.id;
