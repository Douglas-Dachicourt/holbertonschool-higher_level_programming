-- Script that lists all records of the table second_table of the database

-- Commands necessary when the name column is existing 
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
