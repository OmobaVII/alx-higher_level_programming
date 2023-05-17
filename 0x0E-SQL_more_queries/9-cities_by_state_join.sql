-- Lists all cites in hbtn_0d_usa

SELECT id, cities.name, states.name
FROM cities
NATURAL JOIN states
ORDER BY cities.id;
