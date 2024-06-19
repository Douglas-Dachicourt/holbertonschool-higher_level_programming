-- Script that creates the table 'unique_id'

-- Command to create a new table with the 'unique option'
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
