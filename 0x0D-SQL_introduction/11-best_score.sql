-- show top scores
SELECT score, name 
from second_table 
where score >= 10
ORDER BY score desc
