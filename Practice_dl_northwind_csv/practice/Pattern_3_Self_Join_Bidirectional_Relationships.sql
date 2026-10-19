

-- Problem: What product has the most suppliers? (products are bidirectional)
-- Pattern: Self join with UNION for bidirectional relationships

WITH all_products AS (

SELECT
 a.product_id,
 b.supplier_id
FROM      'dl_northwind_csv/data/purchase_order_details.csv' AS a
LEFT JOIN 'dl_northwind_csv/data/purchase_orders.csv'        AS b ON a.purchase_order_id=b.id
GROUP BY ALL

)
-- group by suppliers, and count its products
SELECT 
 product_id,
 COUNT(*) AS num
FROM all_products
GROUP BY ALL
HAVING num>1
ORDER BY num DESC
LIMIT 10;