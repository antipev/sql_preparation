-- Problem: Find uninterrupted runs of orders shipped in perfect order-date sequence
-- Pattern: order_sequence - shipment_sequence grouping technique


WITH order_sequesnce AS (
    SELECT 
        id,
        order_date,
        shipped_date,
        -- Rank 1: The order timeline plan
        ROW_NUMBER() OVER (ORDER BY order_date ASC)   AS order_sequence_plan,
        ROW_NUMBER() OVER (ORDER BY shipped_date ASC) AS shipment_sequence_fact,
        
    FROM 'dl_northwind_csv/data/orders.csv'
    WHERE shipped_date IS NOT NULL

), island_groups AS (
    SELECT 
     *,
     CASE WHEN (shipment_sequence_fact - order_sequence_plan) = 0 
          THEN 0
          ELSE 1 END                                 AS sequence_not_followed,
     
     CASE WHEN (shipment_sequence_fact - order_sequence_plan) > 0 
          THEN 'Delayed'
          WHEN (shipment_sequence_fact - order_sequence_plan) < 0 
          THEN 'Early'
          ELSE 'Normal' END                          AS execution_group_id
    FROM order_sequesnce
    
)

SELECT 
*
FROM island_groups
ORDER BY order_sequence_plan
