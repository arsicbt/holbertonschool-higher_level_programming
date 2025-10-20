-- List records with a score >= 10 in second_table
SELECT name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
