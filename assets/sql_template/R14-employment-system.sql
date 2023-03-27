-- R14 - employment system
SELECT Permits.employee_id, Permission.name
FROM Permission LEFT JOIN Permits ON Permits.permission_id=Permission.id
WHERE Permits.employee_id={employee_id} AND (Permission.name IN (employee_action_set))
