SELECT 
    s."Product ID" AS orphaned_product_id,
    COUNT(*) AS impact_row_count
FROM 'data/candy_sales.csv' AS s
LEFT JOIN 'data/candy_products.csv' AS p 
  ON s."Product ID" = p."Product ID"
WHERE p."Product ID" IS NULL
GROUP BY 1
ORDER BY impact_row_count DESC;


SELECT 
    s."Division" AS orphaned_division,
    COUNT(*) AS impact_row_count
FROM 'data/candy_sales.csv' AS s
LEFT JOIN 'data/candy_targets.csv' AS t 
  ON s."Division" = t."Division"
WHERE t."Division" IS NULL
GROUP BY 1
ORDER BY impact_row_count DESC;


SELECT 
    s."Postal Code" AS orphaned_postal_code,
    COUNT(*) AS impact_row_count
FROM 'data/candy_sales.csv' AS s
LEFT JOIN 'data/uszips.csv' AS z 
  ON s."Postal Code" = z."zip"
WHERE z."zip" IS NULL
GROUP BY 1
ORDER BY impact_row_count DESC;

SELECT 
    p."Factory" AS orphaned_factory_id,
    COUNT(*) AS impact_row_count
FROM 'data/candy_products.csv' AS p
LEFT JOIN 'data/candy_factories.csv' AS f 
  ON p."Factory" = f."Factory"
WHERE f."Factory" IS NULL
GROUP BY 1
ORDER BY impact_row_count DESC;

----------------------

SELECT 
  s.*,
  z.*
FROM 'data/candy_sales.csv' AS s
LEFT JOIN 'data/uszips.csv' AS z 
  ON s."Postal Code" = z."zip"
WHERE z."zip" IS NULL;


------------------
SELECT
county_name,
state_name,
zip
FROM 'data/uszips.csv'
WHERE county_name='Canadian'
GROUP BY ALL
ORDER BY county_name