-- R10 - Insert a user rating by rating id = 45, movie id = 21 and user id = 39
START TRANSACTION;
INSERT INTO RateBy (movie_id, user_id)
SELECT {{movie_id}} AS movie_id, {{user_id}} AS user_id
FROM RateBy
WHERE (movie_id = {{movie_id}} AND user_id = {{user_id}})
HAVING COUNT(*) = 0;
INSERT INTO Rating (id, time, value, comment, movie_id, user_id)
VALUES ({{id}}, NOW(), {{value}}, "{{comment}}", {{movie_id}}, {{user_id}});
COMMIT;