-- Poblem: FIND Medium Product price 
-- Pattern: ROW_NUMBER asc and desc


--step 1 list product prices
WITH products AS (

SELECT 
 id,
 list_price,
 ROW_NUMBER() OVER (ORDER BY list_price ASC)  AS rank_asc, 
 ROW_NUMBER() OVER (ORDER BY list_price DESC) AS rank_desc,
 --
 --PERCENTILE_CONT(0.5) OVER (PARTITION BY id ORDER BY list_price)
 QUANTILE_CONT(list_price, 0.5::DOUBLE) OVER ()
                                              AS median 

FROM 'dl_northwind_csv/data/products.csv'


)
-- step 2 select only non duplicate rows to be used in the model
SELECT
*

FROM products
WHERE rank_asc=rank_desc


