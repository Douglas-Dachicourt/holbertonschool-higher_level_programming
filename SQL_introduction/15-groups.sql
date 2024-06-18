-- Script that lists the number of records with the same score in the table second_table

-- Result that displays the score + number of records for this score with the label number
SELECT COUNT(score) AS number FROM second_table ORDER BY score DESC;
