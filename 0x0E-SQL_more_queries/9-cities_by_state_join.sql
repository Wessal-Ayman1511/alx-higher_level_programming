-- script that lists all cities contained in the database hbtn_0d_usa
-- select with join
select c.id, c.name,  s.name
from cities as c
    inner join states as s
    on c.state_id = s.id
order by c.id ;
