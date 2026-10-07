# Analytics Engineering Technical Screen Playbook

## Data Understanding

### 1. Explore and understand unfamiliar data
* **1.1. List tables**
* **1.2. Check Schema** 
* **1.3. Check Volume and Grain**
* **1.4. Preview raw records**

### 2. Interpret schema and relationships
* **2.1. Identify Primary and Foreign Keys, Verify join cardinality** Ensure join keys use the same data type
* **2.2. Test join integrity** Check the match rate percentage between linked tables.


### 3. Identify missing or inconsistent information

* **3.1. Identify records with missing links** 
* **3.2. Scan for NULL values** Check critical fields for missing values that break metrics.
* **3.3. Detect logical outliers** Look for data that violates business rules or logic.
* **3.4. Evaluate formatting and type consistency** Inspect strings for leading zeros, whitespaces, and case mismatches.

## Data Modeling & Joins and Business Metrics
* **4.1. Translate a business question into data logic**

**Objective** The exercise simulates a real-world analytics engineering problem related to identifying margin leakage across multiple data sources.

* **Theory** https://zenodo.org/records/19951228

"Margin leakage" as preventable ("Margin leakage frequently emerges before it is visible in financial statements.") or partially preventable erosion between **expected contribution margin** and **realized contribution margin** caused by crossfunctional execution gaps, data defects, cost shocks, pricing exceptions, discounts, logistics premiums, disputes, manual adjustments, or delayed intervention.

Margin leakage - a governed cross-system signal-to-action problem.("Traditional margin bridges explain differences between planned and actual profitability after the fact. The new framework shifts the timing: it treats operational signals as early indicators of leakage and converts them into governed intervention cases before the loss becomes embedded.")


"Fragmented Data Sources": The leakage is an architectural problem because signals are distributed across multiple systems, specifically "ERP, procurement, pricing, logistics, inventory, manufacturing, customer-service, finance, and reporting systems"

"Factors" 
A. Procurement may observe a supplier cost increase.
B. Logistics may pay expedited freight. 
C. Sales may approve non-standard discounts. 
D. Billing may issue an invoice with price or quantity discrepancies. 
E. Operations may consume excess labor or substitute materials. 
F. Inventory teams may flag aging or write-down risk. 
G. Customer-service teams may receive deductions or dispute claims.

Each signal is locally visible, but the combined gross-margin effect is often discovered later through monthly close, variance analysis, profitability reports, or manual margin bridges.

"Question": How can cross-system analytics detect and route margin leakage signals before they become embedded financial losses?

"Value"
Reduced **median margin intervention latency** from 55.4 h to 12.6 h relative to spreadsheet margin bridge
reconciliation, reduced **P95 latency** from 148.7 h to 41.8 h, improved **leakage-detection precision** from 62.8% to 86.9%, increased **preventable leakage containment** from 33.6% to 76.4%, and produced USD 7.42 million in annualized **net economic value**.

"Goal" - detecting and routing margin leakage signals across fragmented enterprise systems.

"How"
1. margin signal
2. identification, 
3. cross-system margin pathway mapping, 
3. leakage classification, 
4. margin exposure translation, 
5. finance–operations ownership routing, and 
6. intervention outcome measurement

(
Margin leakage analytics requires strong governance because local Physical Data Element definitions differ across functions
The problem context is crossfunctional margin erosion in fragmented enterprise systems
)

**Margin Leakage (for transaction)** = Expected contribution margin - Realized contribution margin

Expected contribution margin =
Target Price - Authorized Discount - Standard Cost - Planned Freight - Planned Service Cost


Realized contribution margin = 
Realized Net Price - Unplanned Discount - Actual Cost - Actual Freight - Actual Service Cost - Manual Adjustments - Claims


**Margin Leakage (decomposed)** = 
(Target Price - Realized Net Price)             is price leakage, 
(Authorized Discount - Unplanned Discount)      is discount leakage, 
(Standard Cost - Actual Cost)                   is cost leakage, 
(Planned Freight - Actual Freight)              is freight leakage, 
(Planned Service Cost - Actual Service Cost)    is service leakage, 
(Billing Discrepancies)                         is billing leakage, 
(Manual Adjustments)                            is adjustment leakage, 
ϵi                                              is unexplained residual


**Steps to Detect Margin Leakage**
1. Ask clarifying questions before starting
How company defines the Margin leakage?
Does Order table has Price per Unit or Sale (price*units)? The same question for Cost?
What components of contributes to margin?
What other tables are showing actual transactions and what that should be? Is there price period to be applied from dim_product? The same for other shippments and other tables?

---
Always ask:

“Should NULL values be included?”
“What if there are ties?”
“Should the result be ordered?”
“How should we handle empty results?”
---



Mock Interview Format:

Read problem (1 min)
Ask clarifying questions (1 min)
Explain approach (2 min)
Write solution (10 min)
Test and optimize (5 min)
Discuss alternatives (5 min)








● Explain your plan before and while writing code

1. Estimate expected margin, realized margin, and leakage exposure

* Step 1: Unify fragmented data sources. Left join core transaction data with product master data to align local system definitions.

* Step 2: Cast and standardize data types. Explicitly cast all prices, costs, and units to floats to ensure accurate mathematical calculations.

* Step 3: Calculate Expected Contribution Margin. Multiply transactional units by master target prices and standard costs to establish the operational baseline.

* Step 4: Calculate Realized Contribution Margin. Isolate actual performance by extracting processed net prices and recorded operational costs.

* Step 5: Quantify total margin leakage exposure. Subtract the realized contribution margin from the expected contribution margin to surface the cross-system signal.

* Step 6: Audit signal precision. Subtract the calculated realized margin from the reported gross profit to build a validation check against data defects.


2. Classify leakage root cause: price, discount, cost, freight,
   inventory, billing, dispute, production, or adjustment

● Be open to feedback from the interviewer




* **4.2. Validate the correctness of your metric**
A. Recalculate global control totals
- Ensure aggregate sales after modeling exactly match raw sales totals.

B. Implement zero-division safety handles
- Wrap percentage calculations in CASE WHEN statements to handle $0 values safely.

* **4.3. Explain what the results might mean**


