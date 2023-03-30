# Write your MySQL query statement below
SELECT 
    customer_id, (COUNT(v.customer_id) - COUNT(t.visit_id)) AS count_no_trans
FROM 
    Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id  
GROUP BY customer_id
HAVING count_no_trans > 0