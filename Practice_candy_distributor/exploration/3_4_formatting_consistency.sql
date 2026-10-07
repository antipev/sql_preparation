SELECT 
    -- Check if Postal Code length varies (reveals missing leading zeros or format drift)
    MIN(LENGTH("Postal Code")) AS min_zip_len,
    MAX(LENGTH("Postal Code")) AS max_zip_len,
    -- Check for leading/trailing spaces in key fields
    COUNT(CASE WHEN LENGTH("Product ID") != LENGTH(TRIM("Product ID")) THEN 1 END) AS product_id_with_spaces,
    COUNT(CASE WHEN LENGTH("Division") != LENGTH(TRIM("Division")) THEN 1 END) AS division_with_spaces,
    -- Check for customers id length consistency
    MIN(LENGTH(CAST("Customer ID" AS STRING))) AS min_customer_id_len,
    MAX(LENGTH(CAST("Customer ID" AS STRING))) AS max_customer_id_len
FROM 'data/candy_sales.csv';


