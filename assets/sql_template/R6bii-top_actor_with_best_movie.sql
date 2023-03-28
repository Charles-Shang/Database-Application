-- R6ii - Top n movie actors by average user rating on their movies and one best movie
SELECT CONCAT_WS(' ',C.first_name,C.last_name) as actor_name,
    AVG(M.avg_rate) as avg_rating,
    M.name as best_movie_name,
    MAX(M.avg_rate) as best_movie_rating
FROM Actor A
JOIN Acts AC ON A.id = AC.actor_id
JOIN Movie M ON M.id = AC.movie_id
JOIN Celebrity C on A.id = C.id
GROUP BY A.id
ORDER BY avg_rating DESC
LIMIT {{n}};