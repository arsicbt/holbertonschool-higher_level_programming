-- Répertorie les genre de la DB et affiche le nombre d'émissions liées à chacun
SELECT 
    g.name AS genre,
    COUNT(DISTINCT s.show_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres s
    ON g.id = s.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
