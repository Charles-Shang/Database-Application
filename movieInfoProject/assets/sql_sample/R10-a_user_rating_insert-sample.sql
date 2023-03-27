START TRANSACTION;
INSERT INTO RateBy (movie_id, user_id)
VALUES (21, 39);
INSERT INTO Rating (id, time, value, comment, movie_id, user_id)
VALUES (45, NOW(), 7, 'new sample comment', 21, 39);
COMMIT;