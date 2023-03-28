-- R10 - Update a user rating by rating id = 45
UPDATE Rating
SET value = {{value}}, comment = "{{comment}}"
WHERE id = {{id}};