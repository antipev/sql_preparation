-- Poblem: Sort Products by price from more expensive to cheapest
-- Pattern: RANK vs DENSE_RANK vs ROW_NUMBER


--step 1 list products
WITH products AS (

SELECT 
 --COUNT(id)          AS product_count,
 --COUNT(DISTINCT id) AS product_distinct_count
 id,
 list_price
 --ROW_NUMBER() OVER (PARTITION BY email_address ORDER BY id ASC) AS row_number
FROM 'dl_northwind_csv/data/products.csv'
ORDER BY 2 DESC

)
-- step 2 rank 
SELECT
*,
-- rank them and skip rank if ties
RANK() OVER (ORDER BY list_price DESC)       AS rank_one, -- ranks skipped if ties
DENSE_RANK() OVER (ORDER BY list_price DESC) AS rank_two, -- ranks not skipped if ties, but ties get the same rank
ROW_NUMBER() OVER (ORDER BY list_price DESC) AS rank_three, -- ranks are not skipped if ties, but ties get unique number randomly

-- dense rank
FROM products


