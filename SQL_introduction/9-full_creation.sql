-- Script that create a new table + adding some rows with different values

-- Creation of a new table
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
-- Adding a new row in specific values
INSERT INTO second_table VALUES(1, "John", 10);
-- Adding a new row in specific values
INSERT INTO second_table VALUES(2, "Alex", 3);
-- Adding a new row in specific values
INSERT INTO second_table VALUES(3, "Bob", 14);
-- Adding a new row in specific values
INSERT INTO second_table VALUES(4, "George", 8);
