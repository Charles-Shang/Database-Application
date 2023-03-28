-- R10 - Insert a user rating by rating id = 45, movie id = 21 and user id = 39
START TRANSACTION;
INSERT INTO RateBy (movie_id, user_id)
SELECT 21 AS movie_id, 39 AS user_id
FROM RateBy
WHERE (movie_id = 21 AND user_id = 39)
HAVING COUNT(*) = 0;
INSERT INTO Rating (id, time, value, comment, movie_id, user_id)
VALUES (45, NOW(), 7, 'new sample comment', 21, 39);
COMMIT;