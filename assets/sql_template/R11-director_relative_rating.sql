WITH AverageRating(movie_id, average_rating) AS
(
SELECT RateBy.movie_id, AVG(Rating.value)
FROM RateBy, Rating
WHERE RateBy.movie_id = Rating.movie_id AND RateBy.user_id = Rating .user_id AND Rating.value IS NOT NULL
GROUP BY Rating.movie_id
)
SELECT C.id AS director_id, C.first_name AS first_name, C.last_name AS last_name, AVG(A.average_rating) AS relative_rating
FROM Celebrity AS C, Movie as M, AverageRating as A
WHERE C.id = M.director_id  AND A.movie_id = M.id
GROUP BY C.id 
ORDER BY relative_rating DESC