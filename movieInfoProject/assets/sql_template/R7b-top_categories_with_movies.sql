-- R7 - Top m movie category of average ratings and n top movies in each category
WITH temporaryTop3Category(category, averageRating) as
(SELECT category, AVG(rates) FROM MOVIE GROUP BY category ORDER BY AVG(rates) desc LIMIT {{m}})
SELECT category, averageRating, name, rates FROM (
SELECT category, averageRating, name, rates, ROW_NUMBER() OVER (PARTITION BY MOVIE.category ORDER BY MOVIE.rates DESC) AS num
FROM temporaryTop3Category NATURAL JOIN MOVIE 
ORDER BY averageRating DESC, rates DESC
) AS withNum
WHERE withNum.num <= {{n}}