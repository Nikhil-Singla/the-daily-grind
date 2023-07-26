# Most Optimal Attempt
# Write your MySQL query statement below
SELECT E.name AS "Employee"
FROM Employee E, Employee E2
WHERE E.managerId = E2.id AND E.salary > E2.salary 


# Initial Attempt
# Write your MySQL query statement below
SELECT E.name AS "Employee"
FROM Employee E
INNER JOIN Employee em
ON E.managerId = em.id
WHERE E.salary > em.Salary 