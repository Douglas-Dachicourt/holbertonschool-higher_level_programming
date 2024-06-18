-- Script that create a table if not already exists

-- Command to create a table 
IF NOT EXISTS first_table
BEGIN
    CREATE TABLE first_table (id INT, name VARCHAR(256));
END
