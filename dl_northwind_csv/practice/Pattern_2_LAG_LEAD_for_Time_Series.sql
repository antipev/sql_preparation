-- Problem: Find dates where sales was higher than previous day
-- Pattern: LAG(sale, 1) OVER (ORDER BY recordDate)


--step 1: find sales by dates

WITH order_details AS(

SELECT 
 order_id,
 SUM(unit_price*quantity) AS sales
 
FROM 'dl_northwind_csv\data\order_details.csv'
GROUP BY ALL

), orders AS (

SELECT 
 id AS order_id,
 order_date
FROM 'dl_northwind_csv\data\orders.csv'

), order_by_dates AS (

SELECT 
 b.order_date,
 SUM(a.sales) AS daily_sales

 
FROM order_details AS a
INNER JOIN orders   AS b ON a.order_id=b.order_id

GROUP BY ALL
ORDER BY 1

--step 2: find sales by dates and previous date sales

), order_by_dates_comparison AS (

SELECT 
 order_date,
 daily_sales,

 LAG(daily_sales, 1) OVER (ORDER BY order_date ASC) AS previous_day_sales,
 LAG(order_date, 1)  OVER (ORDER BY order_date ASC) AS previous_day,


 -- Safely fetches sales from exactly 1 day ago based on the calendar date value
-- LAG(daily_sales, 1) OVER (
--     ORDER BY RANGE BETWEEN INTERVAL 1 DAY PRECEDING AND 1 DAY PRECEDING
-- ) AS previous_day_sales

FROM order_by_dates


)

SELECT
*
FROM order_by_dates_comparison
WHERE daily_sales>previous_day_sales
AND previous_day_sales IS NOT NULL
ORDER BY order_date

