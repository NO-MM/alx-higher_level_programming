-- Import the database dump from hbtn_0d_tvshows
-- in MySQL server(comedy).
SELECT tv_shows.title
FROM tv_shows
     JOIN tv_show_genres
     ON tv_show.id = tv_show_genres.show_id

     JOIN tv_genres
     ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Comedy'
ORDER BY tv_shows.title ASC;
