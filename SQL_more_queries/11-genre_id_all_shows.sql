-- Lister tout les shows, y compris ceux qui n'ont pas de genre
SELECT tv_shows.title, tv_show_genres_genre_id
FROM tv_show_genresLEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id
