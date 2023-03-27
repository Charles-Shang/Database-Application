START TRANSACTION;
INSERT INTO RateBy (movie_id, user_id)
VALUES ({movid_id}, {user_id});
INSERT INTO Rating (id, time, value, comment, movie_id, user_id)
VALUES ({id}, NOW(), {value}, "{comment}", {movie_id}, {user_id});
COMMIT;