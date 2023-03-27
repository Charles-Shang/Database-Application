-- R14 - employment system
SELECT Permits.employee_id, Permission.name
FROM Permission LEFT JOIN Permits ON Permits.permission_id=Permission.id
WHERE Permits.employee_id=2 AND (Permission.name IN ('permission6', 'permission9'));