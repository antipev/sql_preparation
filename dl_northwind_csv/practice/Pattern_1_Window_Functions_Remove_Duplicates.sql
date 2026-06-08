

-- Problem: Delete duplicate emails, keeping the one with smallest id
-- Pattern: ROW_NUMBER() OVER (PARTITION BY email ORDER BY id)


--step 1 access original table
WITH employees AS (

SELECT
 id,
 ROW_NUMBER() OVER (PARTITION BY email_address ORDER BY id ASC) AS row_number
FROM 'dl_northwind_csv/data/employees.csv'

)
-- step 2 select only non duplicate rows to be used in the model
SELECT
*
FROM employees
WHERE row_number=1
