-- lists all records of second tablee
select score, name
from second_table
where name is not NULL
order by score DESC
