# Write your MySQL query statement below
SELECT name FROM Customer
WHERE Customer.referee_id IS NULL OR
Customer.referee_id != 2


# Fastest Answer? Write your MySQL query statement below
SELECT c.name
FROM Customer c
WHERE c.referee_id != 2
    OR c.referee_id is NULL
