-- Lists all cites in hbtn_0d_usa

SELECT id, cities.name, states.name
FROM cities
NATURAL JOIN states
WHERE cities.state_id = cities.id
ORDER BY cities.id;
