-- lists all records of second tablee
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
