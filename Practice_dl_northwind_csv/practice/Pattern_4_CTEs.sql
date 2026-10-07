-- Problem: Monthly transaction summaries
-- Pattern: CTE for multi-step aggregations

WITH monthly_stats AS (
    SELECT 
        DATE_TRUNC('month',order_date) as month,
        ship_country_region,
        --status_id,
        COUNT(*)                                                   AS order_count,
        COUNT(CASE WHEN status_id = 0 THEN id ELSE NULL END)       AS new_order_count,
        COUNT(CASE WHEN status_id = 3 THEN id ELSE NULL END)       AS closed_order_count,
        COUNT(CASE WHEN status_id IN(1,2) THEN id ELSE NULL END)   AS wip_order_count,
    FROM 'dl_northwind_csv/data/orders.csv'
    GROUP BY ALL
)
SELECT 
 * 
FROM monthly_stats
ORDER BY 1