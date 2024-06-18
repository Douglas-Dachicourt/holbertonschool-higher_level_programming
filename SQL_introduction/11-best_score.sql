-- Script that lists all records with a score >= 10 in the table second_table

-- Display both scores & names ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 AND score ORDER BY DESC;
