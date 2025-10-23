-- Répertorie les genre de la DB et affiche le nombre d'émissions liées à chacun
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres
    ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
ORDER BY number_of_shows DESC;
