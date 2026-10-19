-- Step 1: calculate margin for each sale

WITH order_margin AS (
    
    
SELECT
--dimesions
a."Order ID",
a."Product ID",
a."Product Name",
a.Sales,
a.Units,
a.Cost,
---metrics

ROUND(CAST(a.Sales AS FLOAT),4)                       AS Realized_Net_Price, -- actual sale processed
ROUND(CAST(a.Cost  AS FLOAT),4)                       AS Actual_cost,-- actual costs recorded when sales processed

ROUND(CAST(a.Units*b."Unit Price"  AS FLOAT),4)       AS Target_Price, -- what supposed to be processed as sales to reflect recent prices
ROUND(CAST(a.Units*b."Unit Cost"   AS FLOAT),4)       AS Standard_Cost, -- what costs suppposed to be for sales

ROUND(CAST(a."Gross Profit"   AS FLOAT),4)            AS Gross_Profit_to_compare_with_relized_contribution_margin,

FROM 'data/candy_sales.csv' AS a 
LEFT JOIN 'data/candy_products.csv' AS b ON a."Product ID" = b."Product ID"
WHERE 1=1
--AND a."Order ID"='US-2023-121671-CHO-NUT-13000'
GROUP BY ALL


), order_margin_calculations AS (

SELECT 

--dimesions
"Order ID",
"Product ID",
"Product Name",
Sales,
Units,
Cost,
---metrics
Realized_Net_Price,
Actual_cost,
Realized_Net_Price-Actual_cost AS Realized_contribution_margin,

Target_Price,
Standard_Cost,
Target_Price-Standard_Cost     AS Expected_contribution_margin,



Gross_Profit_to_compare_with_relized_contribution_margin,


FROM order_margin

)

SELECT
*,
ROUND(CAST((Gross_Profit_to_compare_with_relized_contribution_margin
-Realized_contribution_margin) AS FLOAT),4) AS check

FROM order_margin_calculations
WHERE 1=1
--AND ROUND(CAST((Gross_Profit_to_compare_with_relized_contribution_margin
---Realized_contribution_margin) AS FLOAT),4)
--<>0
AND Realized_contribution_margin<>Expected_contribution_margin
ORDER BY Realized_contribution_margin ASC