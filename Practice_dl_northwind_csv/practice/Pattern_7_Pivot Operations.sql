-- Problem: Pivot order by ship name and by month
-- Pattern: CASE WHEN for manual pivoting

SELECT 
    ship_name,
    COUNT(CASE WHEN EXTRACT(month FROM order_date) = 1 THEN id ELSE NULL END) as Jan_Orders,
    COUNT(CASE WHEN EXTRACT(month FROM order_date) = 2 THEN id ELSE NULL END) as Feb_Orders,
    COUNT(CASE WHEN EXTRACT(month FROM order_date) = 3 THEN id ELSE NULL END) as Mar_Orders
FROM 'dl_northwind_csv/data/orders.csv'
GROUP BY ALL