select id, problem_postcode , full_postcode, min(distance) 
from 
(select id, problem_postcode , full_postcode, (problem.lat-solution.lat)*(problem.lat-solution.lat)+(problem.lon-solution.lon)*(problem.lon-solution.lon) as distance
from
(select value as problem_postcode, id, key, lat, lon
from nodes_tags join nodes using(id)
where key = "postcode" and length(value)<=4 ) as problem
inner join 
(select substr(value,1,4) as match_postcode, value as full_postcode, key, lat, lon
from nodes_tags join nodes using(id)
where key = "postcode" and length(value)>4) as solution
on problem_postcode = match_postcode) as lat_lon_distances
group by problem_postcode
