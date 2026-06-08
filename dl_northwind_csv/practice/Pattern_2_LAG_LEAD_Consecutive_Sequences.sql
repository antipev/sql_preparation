-- Problem: Find sequences where daily sales exceed $1,000 for at least 3 consecutive days
-- Pattern: LAG/LEAD to detect consecutive sequence conditions


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
 SUM(a.sales) AS daily_sales,
 CASE WHEN SUM(a.sales) > 1000 THEN 1 ELSE 0 END AS is_high_sales_day
 
FROM order_details AS a
INNER JOIN orders   AS b ON a.order_id=b.order_id

GROUP BY ALL
ORDER BY 1

--step 2: LAG to look back at the condition flag over the last 2 periods
), consecutive_check AS (
    SELECT 
        order_date,
        daily_sales,
        is_high_sales_day,
        LAG(is_high_sales_day, 1) OVER (ORDER BY order_date ASC) AS prev1_was_high,
        LAG(is_high_sales_day, 2) OVER (ORDER BY order_date ASC) AS prev2_was_high
    FROM order_by_dates
)

--step 3: filter for rows where all 3 previous periods were ALL high sales days
SELECT  
        order_date,
        daily_sales,
        is_high_sales_day,
        prev1_was_high,
        prev2_was_high
FROM consecutive_check
WHERE is_high_sales_day = 1 
  AND prev1_was_high = 1 
  AND prev2_was_high = 1
ORDER BY order_date
