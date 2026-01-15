# Write your MySQL query statement below
SELECT e.name AS Employee FROM Employee e
JOIN Employee m
ON e.managerID=m.id
WHERE e.Salary>m.salary
