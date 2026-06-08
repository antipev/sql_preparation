

-- Problem: Find employees earning more than their managers
-- Pattern: Self join on manager_id = employee_id


--step 1 create emplyee table with managers id
WITH employees AS (

SELECT
 *,
 CASE WHEN id IN(6,7,9) THEN 8
      WHEN id IN(1,3,4) THEN 5
      WHEN id IN(8,5) THEN 2
      ELSE 0
      END  AS manager_id,


FROM 'dl_northwind_csv/data/employees.csv' 

-- step 2 since we do not have salary we assume that all employees are sales people 
-- earning money as 2% from sales
-- assuming all data has correct keys, no missing data

), orders AS (

    
SELECT
 employee_id,
 id                                     AS order_id,
 DATE(DATE_TRUNC('month', order_date))  AS order_month
FROM 'dl_northwind_csv/data/orders.csv' 


), order_details AS (

SELECT
 order_id,
 SUM(unit_price * quantity)             AS sales
FROM 'dl_northwind_csv/data/order_details.csv'
GROUP BY ALL

), order_salary AS (
SELECT
 a.employee_id,
 a.order_id,
 a.order_month,
 b.sales,
 b.sales* 0.02                          AS salary
FROM order_details              AS b -- the most granular table Hunter
LEFT JOIN orders                AS a ON a.order_id=b.order_id -- the Prey table
ORDER BY 1,3

), monthly_employee_salary AS(

SELECT
 employee_id,
 order_month,
 SUM(salary) AS sum_salary
FROM order_salary
GROUP BY ALL
ORDER BY 1,2

), avg_monthly_employee_salary AS(

SELECT
 employee_id,
 COUNT(order_month) AS month_count,
 SUM(sum_salary)    AS sum_salary,
 CASE WHEN COUNT(order_month)=0
      THEN 0
      ELSE SUM(sum_salary)/COUNT(order_month)
 END                AS average_salary

FROM monthly_employee_salary
GROUP BY ALL
ORDER BY 1


), employee_with_salary AS(

SELECT
 a.id                         AS employee_id,
 a.job_title,
 a.manager_id,
 COALESCE(b.average_salary,0) AS average_salary,

FROM employees                             AS a
LEFT JOIN avg_monthly_employee_salary      AS b ON a.id=b.employee_id
ORDER BY 1,2

-- step 3. Once we got out dim table with salaries
-- we need to Find employees earning more than their managers

), compared_salaries AS (

SELECT
 a.employee_id,
 a.job_title,
 a.average_salary AS employee_salary,
 b.average_salary AS manager_salary
FROM employee_with_salary      AS a
LEFT JOIN employee_with_salary AS b ON a.manager_id = b.employee_id

)


SELECT
*
FROM compared_salaries
WHERE employee_salary > manager_salary
