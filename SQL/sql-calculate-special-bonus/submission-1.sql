-- Write your query below
SELECT employee_id,
CASE
    WHEN SUBSTRING( name ,1 ,1) != 'M' AND employee_id % 2 = 1 THEN salary
    ELSE 0
END AS Bonus
FROM employees
ORDER BY employee_id ASC
