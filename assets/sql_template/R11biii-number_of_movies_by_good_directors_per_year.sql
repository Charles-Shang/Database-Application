-- R11iii - Number of movies directed by directors with top {n} (in percentage) relative rating for each year
WITH AverageRating(movie_id, average_rating) AS
(
SELECT RateBy.movie_id, AVG(Rating.value)
FROM RateBy, Rating
WHERE RateBy.movie_id = Rating.movie_id AND RateBy.user_id = Rating .user_id AND Rating.value IS NOT NULL
GROUP BY Rating.movie_id
),
DirectorRating(director_id, director_first_name, director_last_name, relative_rating, relative_rank) AS 
(
SELECT C.id, C.first_name, C.last_name, AVG(A.average_rating) as relative_rating, RANK() OVER (ORDER BY (AVG(A.average_rating)) DESC)
FROM Celebrity AS C, Movie as M, AverageRating as A
WHERE C.id = M.director_id  AND A.movie_id = M.id
GROUP BY C.id 
ORDER BY relative_rating DESC
)
SELECT year, COUNT(*) AS num
FROM Movie
WHERE director_id IN
(
SELECT director_id FROM DirectorRating WHERE relative_rank <= (SELECT COUNT(*) FROM DirectorRating)* {{n}}
)
GROUP BY year
ORDER BY year;