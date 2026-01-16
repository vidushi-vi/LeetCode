# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums FROM (
    SELECT num,
    LAG(num,1) OVER() AS l1,
    LAG(num,2) OVER() AS l2
    FROM Logs) t 
WHERE num=l1 AND num=l2;