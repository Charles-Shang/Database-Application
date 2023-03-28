-- R14 - employment system check if the employee has all the inputed permissions
SELECT count(*) as rowNum
FROM (
    SELECT Permits.employee_id, Permission.name
    FROM Permission LEFT JOIN Permits ON Permits.permission_id=Permission.id
    WHERE Permits.employee_id=2 AND (Permission.name IN ('permission6', 'permission9'))
) as A;