

SELECT 
    MIN(s."Order Date") AS min_order_date,
    MAX(s."Order Date") AS max_order_date,
    --
    MIN(s."Ship Date") AS min_ship_date,
    MAX(s."Ship Date") AS max_ship_date
FROM 'data/candy_sales.csv' AS s
GROUP BY ALL;


SELECT 
    s."Order Date",
    s."Ship Date",
    s."Order ID"
FROM 'data/candy_sales.csv' AS s
WHERE s."Ship Date" < s."Order Date";

SELECT 
    s."Order Date",
    s."Ship Date",
    s."Order ID"
FROM 'data/candy_sales.csv' AS s
WHERE EXTRACT(YEAR FROM s."Ship Date") - EXTRACT(YEAR FROM s."Order Date") >1;
