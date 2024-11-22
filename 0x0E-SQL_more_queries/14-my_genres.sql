-- Import the database dump from hbtn_0d_tvshows
-- in MySQL server(genres).
SELECT tv_genres.name
FROM tv_shows
     JOIN tv_show_genres
     ON tv_genre.id = tv_show_genres.genre_id

     JOIN tv_genres
     ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
