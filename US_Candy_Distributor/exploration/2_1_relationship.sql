
/*
candy_sales FK: "Product_ID" => candy_products PK: "Product_ID"
candy_sales FK: "Division" => candy_targets PK: "Division"
candy_sales FK: "Postal Code" => uszips PK: "zip"
candy_products FK: "Factory" => candy_factories PK: "Factory"
*/

SELECT
"Product ID" 
FROM 'data/candy_products.csv'