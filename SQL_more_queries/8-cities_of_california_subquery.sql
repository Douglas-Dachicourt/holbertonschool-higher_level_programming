-- Script that lists all the cities of California that can be found in the database 'hbtn_0d_usa'

-- Create database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use this database
USE hbtn_0d_usa;
-- Command 'Select' combined to 'Where' and 'Order by'
SELECT * FROM states
WHERE name = 'California'
ORDER BY cities.id;
