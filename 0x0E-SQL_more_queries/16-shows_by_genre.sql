-- Import the database dump from hbtn_0d_tvshows
-- in MySQL server(Shows, Genres).
SELECT tv_shows.title, tv_genre.name
FROM tv_shows
     LEFT JOIN tv_show_genres
     ON tv_show.id = tv_show_genres.show_id

     LEFT JOIN tv_genres
     ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genre.name ASC;

