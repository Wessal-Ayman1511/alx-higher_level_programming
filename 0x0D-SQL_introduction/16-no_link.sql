-- lists all records of second table
select score, name
from second_table
where name is not NULL
order by score DESC
