-- a script that lists the number of records with the same score in the table second_table
SELECT score, COUNT(1) As number FROM second_table
GROUP BY score
ORDER BY number DESC;
