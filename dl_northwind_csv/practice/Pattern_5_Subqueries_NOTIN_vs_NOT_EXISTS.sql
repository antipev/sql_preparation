
-- SLOW: NOT IN with subquery (scans entire subquery for each row)
SELECT id AS order_id
FROM 'dl_northwind_csv/data/orders.csv'
WHERE id NOT IN (SELECT order_id FROM 'dl_northwind_csv/data/order_details.csv')
ORDER BY 1
;
-- FAST: NOT EXISTS (short-circuits on first match)
SELECT c.id AS order_id
FROM 'dl_northwind_csv/data/orders.csv' AS c
WHERE NOT EXISTS (
    SELECT 1 FROM 'dl_northwind_csv/data/order_details.csv' o WHERE o.order_id = c.id
)
ORDER BY 1
;

-- FASTEST: LEFT JOIN with NULL check
SELECT c.id AS order_id
FROM  'dl_northwind_csv/data/orders.csv' AS c
LEFT JOIN 'dl_northwind_csv/data/order_details.csv' o ON o.order_id = c.id
WHERE o.order_id IS NULL
;


----

-- SELECT 
--     name AS Customers
-- FROM Customers
-- WHERE id NOT IN (
--     SELECT DISTINCT customerId 
--     FROM Orders
-- );

-- SELECT 
--     c.name AS Customers
-- FROM Customers AS c
-- WHERE NOT EXISTS (
--     SELECT 1 
--     FROM Orders AS o 
--     WHERE o.customerId = c.id
-- );

-- SELECT 
--     c.name AS Customers
-- FROM Customers AS c
-- LEFT JOIN Orders AS o ON c.id = o.customerId
-- WHERE o.customerId IS NULL;