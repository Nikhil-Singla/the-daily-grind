# Write your MySQL query statement below
SELECT 
    name, SUM(amount) AS 'balance'
FROM 
    Users
NATURAL JOIN Transactions
GROUP BY name
HAVING balance > 10000



# OPTIMAL SOLUTION (LEETCODE)
# Write your MySQL query statement below
SELECT 
    name        AS  "NAME",
    SUM(amount) AS  "BALANCE"
FROM 
    users u INNER JOIN transactions t 
    ON u.account = t.account
GROUP BY name
HAVING balance > 10000