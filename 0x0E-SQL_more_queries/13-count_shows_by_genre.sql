-- Import the database dump from hbtn_0d_tvshows
-- in MySQL server.
SELECT tv_genres.name, As genre, COUNT(show_id) As number_of_shows
FROM tv_genres JOIN tv_show_genres ON tv_genre.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
