-- 1. Check candy_factories
SELECT count(*) as total_rows, count(distinct factory) as unique_keys FROM 'data/candy_factories.csv';

-- 2. Check candy_products
SELECT count(*) as total_rows, count(distinct "Product ID") as unique_keys FROM 'data/candy_products.csv';

-- 3. Check candy_sales
SELECT count(*) as total_rows, count(distinct "Row ID") as unique_keys FROM 'data/candy_sales.csv';

-- 4. Check uszips
SELECT count(*) as total_rows, count(distinct zip) as unique_keys FROM 'data/uszips.csv';

-- 5. targets
SELECT count(*) as total_rows, count(distinct division) as unique_keys FROM 'data/candy_targets.csv';