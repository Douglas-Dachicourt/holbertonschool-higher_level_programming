-- Script that lists all shows contained in the database hbtn_0d_tvshows

-- Using 'JOIN' method
SELECT tv_shows.title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id
