
-- candy_sales FK: "Product_ID" => candy_products PK: "Product_ID"

SELECT 
    COUNT(s."Product ID") AS total_sales_rows,
    COUNT(p."Product ID") AS matched_product_rows,
    (COUNT(p."Product ID") * 100.0 / COUNT(s."Product ID")) AS match_rate_percentage
FROM 'data/candy_sales.csv' AS s
LEFT JOIN 'data/candy_products.csv' AS p ON s."Product ID" = p."Product ID"

;

--candy_sales FK: "Division" => candy_targets PK: "Division"

SELECT 
    COUNT(s."Division") AS total_sales_rows,
    COUNT(t."Division") AS matched_target_rows,
    (COUNT(t."Division") * 100.0 / COUNT(s."Division")) AS match_rate_percentage
FROM 'data/candy_sales.csv' AS s
LEFT JOIN 'data/candy_targets.csv' AS t 
  ON s."Division" = t."Division"

;

--candy_sales FK: "Postal Code" => uszips PK: "zip"
SELECT 
    COUNT(s."Postal Code") AS total_sales_rows,
    COUNT(z."zip") AS matched_zip_rows,
    (COUNT(z."zip") * 100.0 / COUNT(s."Postal Code")) AS match_rate_percentage
FROM 'data/candy_sales.csv' AS s
LEFT JOIN 'data/uszips.csv' AS z 
  ON s."Postal Code" = z."zip"

;

--candy_products FK: "Factory" => candy_factories PK: "Factory"


SELECT 
    COUNT(p."Factory") AS total_product_rows,
    COUNT(f."Factory") AS matched_factory_rows,
    (COUNT(f."Factory") * 100.0 / COUNT(p."Factory")) AS match_rate_percentage
FROM 'data/candy_products.csv' AS p
LEFT JOIN 'data/candy_factories.csv' AS f 
  ON p."Factory" = f."Factory";