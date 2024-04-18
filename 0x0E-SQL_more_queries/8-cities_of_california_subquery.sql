-- list cities in california
SELECT id, name
from cities
where state_id = 1
order by id asc
