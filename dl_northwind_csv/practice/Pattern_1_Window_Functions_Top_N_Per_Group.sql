
-- Problem: Find top 3 salaries in each department
-- Pattern: ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC)


-- step 1 since we do not have salary we assume that all employees are sales people 
-- earning money as 2% from sales
-- assuming all data has correct keys, no missing data

WITH orders AS (

    
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
 a.company, -- assuming no department available, so we use company
 COALESCE(b.average_salary,0) AS average_salary
FROM 'dl_northwind_csv/data/employees.csv' AS a
LEFT JOIN avg_monthly_employee_salary      AS b ON a.id=b.employee_id
ORDER BY 1,2

-- step 2. Once we got out dim table with salaries
-- we need to calculate top 3 salaries in each department/company

), ranked_salaries AS (

SELECT
 employee_id,
 company,
 average_salary,
 ROW_NUMBER() OVER (PARTITION BY company ORDER BY average_salary DESC) AS rn,
FROM employee_with_salary

)


SELECT
*
FROM ranked_salaries
WHERE rn <= 3
