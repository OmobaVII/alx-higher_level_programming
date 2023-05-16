-- List all records of second_table only those with name

SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
