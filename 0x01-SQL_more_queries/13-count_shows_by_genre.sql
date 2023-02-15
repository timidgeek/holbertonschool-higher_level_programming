-- 13-count_shows_by_genre.sql, Lindsey Thomas C19
-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre,
COUNT(show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
