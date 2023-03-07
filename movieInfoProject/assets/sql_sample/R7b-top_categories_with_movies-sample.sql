-- R7 - Top 5 movie category of average ratings and 3 top movies in each category
WITH MOVIE(name, category, rates) as
(SELECT Movie.name, Movie_category.category, Movie.avg_rate FROM Movie, Movie_category WHERE Movie.id = Movie_category.movie_id),
temporaryTop3Category(category, averageRating) as
(SELECT category, AVG(rates) FROM MOVIE GROUP BY category ORDER BY AVG(rates) desc LIMIT 5)
SELECT category, averageRating, name, rates FROM (
SELECT category, averageRating, name, rates, ROW_NUMBER() OVER (PARTITION BY MOVIE.category ORDER BY MOVIE.rates DESC) AS num
FROM temporaryTop3Category NATURAL JOIN MOVIE 
ORDER BY averageRating DESC, rates DESC
) AS withNum
WHERE withNum.num <= 3