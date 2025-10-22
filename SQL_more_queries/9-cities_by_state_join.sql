-- Lister les villes
SELECT cities.id, cities.name, states.name
FROM cities, statesWHERE cities.state_id = states.id
ORDER BY cities.id ASC;
