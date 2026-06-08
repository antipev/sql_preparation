--SHOW TABLES IN catalog_name.schema_name;

SELECT 
  filename,
  size, 
  content, 
FROM read_blob('data/*.csv');