-- Script that computes the score average of all records in the table second_table

-- Command AVG to select the int column we want the average
WITH average AS AVG(score) FROM second_table;
