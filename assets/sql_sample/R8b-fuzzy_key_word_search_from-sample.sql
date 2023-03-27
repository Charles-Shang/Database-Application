--R8-a fuzzy search

WITH midList(mids) as (
(SELECT DISTINCT Movie.id
 FROM Movie
 WHERE Movie.name LIKE '%5%')
 UNION 
 (SELECT DISTINCT movie_id
 FROM  Celebrity c  join Acts a on c.id = a.actor_id
 WHERE c.name LIKE '%5%')
 UNION 
 (SELECT DISTINCT Movie.id
 FROM Celebrity c2  JOIN Movie on Movie.director_id = c2.id
 WHERE c2.name LIKE '%5%')
)

SELECT m.name as title, m.region, m.year, m.avg_rate , m.introduction , m.category, d.name as director_name,
GROUP_CONCAT(DISTINCT a.name) as actor_name
FROM (Select * from Movie m1 inner join Movie_category mc2 on mc2.movie_id = m1.id) as m,
	midList,Actor natural join Celebrity as a, Acts ar, Director natural join Celebrity as d
WHERE ar.actor_id  = a.id  and ar.movie_id  = m.id  and m.director_id  = d.id  and m.id  = midList.mids
GROUP BY(m.name);


