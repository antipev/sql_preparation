SELECT 
    COUNT(*) AS total_rows,
    -- Structural Key Null Counts
    SUM(CASE WHEN "Row ID" IS NULL THEN 1 ELSE 0 END) AS null_row_id,
    SUM(CASE WHEN "Order ID" IS NULL THEN 1 ELSE 0 END) AS null_order_id,
    SUM(CASE WHEN "Product ID" IS NULL THEN 1 ELSE 0 END) AS null_product_id,
    SUM(CASE WHEN "Postal Code" IS NULL THEN 1 ELSE 0 END) AS null_postal_code,
    SUM(CASE WHEN "Division" IS NULL THEN 1 ELSE 0 END) AS null_division,
    -- Financial/Metric Null Counts
    SUM(CASE WHEN "Sales" IS NULL THEN 1 ELSE 0 END) AS null_sales,
    SUM(CASE WHEN "Units" IS NULL THEN 1 ELSE 0 END) AS null_units,
    SUM(CASE WHEN "Cost" IS NULL THEN 1 ELSE 0 END) AS null_cost,
    SUM(CASE WHEN "Gross Profit" IS NULL THEN 1 ELSE 0 END) AS null_gross_profit
FROM 'data/candy_sales.csv';


SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN "Product ID" IS NULL THEN 1 ELSE 0 END) AS null_product_id,
    SUM(CASE WHEN "Product Name" IS NULL THEN 1 ELSE 0 END) AS null_product_name,
    SUM(CASE WHEN "Division" IS NULL THEN 1 ELSE 0 END) AS null_division,
    SUM(CASE WHEN "Factory" IS NULL THEN 1 ELSE 0 END) AS null_factory,
    SUM(CASE WHEN "Unit Price" IS NULL THEN 1 ELSE 0 END) AS null_unit_price,
    SUM(CASE WHEN "Unit Cost" IS NULL THEN 1 ELSE 0 END) AS null_unit_cost
FROM 'data/candy_products.csv';

SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN "Division" IS NULL THEN 1 ELSE 0 END) AS null_division,
    SUM(CASE WHEN "Target" IS NULL THEN 1 ELSE 0 END) AS null_target
FROM 'data/candy_targets.csv';

-- Check Factories
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN "Factory" IS NULL THEN 1 ELSE 0 END) AS null_factory,
    SUM(CASE WHEN "Latitude" IS NULL THEN 1 ELSE 0 END) AS null_latitude,
    SUM(CASE WHEN "Longitude" IS NULL THEN 1 ELSE 0 END) AS null_longitude
FROM 'data/candy_factories.csv';

-- Check US Zips
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN "zip" IS NULL THEN 1 ELSE 0 END) AS null_zip,
    SUM(CASE WHEN "city" IS NULL THEN 1 ELSE 0 END) AS null_city,
    SUM(CASE WHEN "state_id" IS NULL THEN 1 ELSE 0 END) AS null_state,
    SUM(CASE WHEN "lat" IS NULL THEN 1 ELSE 0 END) AS null_latitude,
    SUM(CASE WHEN "lng" IS NULL THEN 1 ELSE 0 END) AS null_longitude
FROM 'data/uszips.csv';