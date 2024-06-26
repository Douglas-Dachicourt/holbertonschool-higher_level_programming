-- Script that uses the 'hbtn_0d_tvshows' database to lists all genres of movie 'Dexter'

-- Combination of 2 'JOIN ' method + 'WHERE' clause
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY name
