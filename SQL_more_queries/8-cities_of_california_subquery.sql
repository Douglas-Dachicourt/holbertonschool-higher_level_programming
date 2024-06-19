-- Script that lists all the cities of California that can be found in the database 'hbtn_0d_usa'

-- Use database 'hbtn_0d_usa'
USE hbtn_0d_usa;
-- Command 'Select' combined to 'Where' and 'Order by'
SELECT name
FROM states, cities
WHERE name = 'California'
ORDER BY cities.id;
