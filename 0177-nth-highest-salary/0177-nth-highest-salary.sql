CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
   /*SELECT (
        SELECT DISTINCT Salary FROM Employee 
        ORDER BY Salary DESC
        LIMIT N-1, 1
    )*/
    SELECT (
        SELECT salary AS getNthHighestSalary FROM(
            SELECT DISTINCT salary,
            DENSE_RANK() OVER(ORDER BY salary DESC) AS r
            FROM Employee) t
        WHERE r=N
        
    )

);
END