# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees E1
LEFT JOIN EmployeeUNI E2 ON E1.id = E2.id 