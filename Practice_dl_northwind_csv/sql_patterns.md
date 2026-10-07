# SQL Interview Patterns Cheat Sheet

## 🔥 Pattern #1: Window Functions

### The Classic: Remove Duplicates
* Pattern: ROW_NUMBER() OVER (PARTITION BY email ORDER BY id)

-- Problem: Delete duplicate emails, keeping the one with smallest id
-- Pattern: ROW_NUMBER() OVER (PARTITION BY email ORDER BY id)

-- Better solution using window functions:
WITH ranked AS (
    SELECT id, 
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as rn
    FROM Person
)
DELETE FROM Person 
WHERE id IN (SELECT id FROM ranked WHERE rn > 1);


### The Money Question: Top N Per Group
* Pattern: ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC)

-- Problem: Find top 3 salaries in each department
-- Pattern: ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC)

WITH ranked_salaries AS (
    SELECT 
        department,
        employee_name,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rn
    FROM employees
)
SELECT department, employee_name, salary
FROM ranked_salaries
WHERE rn <= 3;


### The Tricky One: RANK vs DENSE_RANK vs ROW_NUMBER
-- Sample data: Scores [100, 100, 90, 80]

-- ROW_NUMBER(): Always unique (1, 2, 3, 4)
SELECT score, ROW_NUMBER() OVER (ORDER BY score DESC)
-- Output: 100→1, 100→2, 90→3, 80→4

-- RANK(): Same rank for ties, skip next (1, 1, 3, 4)  
SELECT score, RANK() OVER (ORDER BY score DESC)
-- Output: 100→1, 100→1, 90→3, 80→4

-- DENSE_RANK(): Same rank for ties, no skip (1, 1, 2, 3)
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC)
-- Output: 100→1, 100→1, 90→2, 80→3

---

## ⏱️ Pattern #2: LAG/LEAD for Time Series

### The Classic: Rising Temperature
* Pattern: LAG(temperature, 1) OVER (ORDER BY recordDate)

-- Problem: Find dates where temperature was higher than previous day
-- Pattern: LAG(temperature, 1) OVER (ORDER BY recordDate)

WITH temp_comparison AS (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(temperature, 1) OVER (ORDER BY recordDate) as prev_temp,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) as prev_date
    FROM Weather
)
SELECT id
FROM temp_comparison
WHERE temperature > prev_temp 
  AND recordDate = DATE_ADD(prev_date, INTERVAL 1 DAY);


### The Hard One: Consecutive Sequences
* Pattern: LAG/LEAD to detect consecutive sequences

-- Problem: Find all numbers that appear at least 3 times consecutively
-- Pattern: LAG/LEAD to detect consecutive sequences

WITH consecutive_check AS (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) as prev1,
        LAG(num, 2) OVER (ORDER BY id) as prev2
    FROM Logs
)
SELECT DISTINCT num as ConsecutiveNums
FROM consecutive_check
WHERE num = prev1 AND num = prev2;

---

## 🔗 Pattern #3: Self Joins

### The Gimme: Employees Earning More Than Managers
* Pattern: Self join on manager_id = employee_id

-- Problem: Find employees earning more than their managers
-- Pattern: Self join on manager_id = employee_id

SELECT e1.name as Employee
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;


### The Tricky One: Bidirectional Relationships
* Pattern: Self join with UNION for bidirectional relationships

-- Problem: Who has the most friends? (friendships are bidirectional)
-- Pattern: Self join with UNION for bidirectional relationships

WITH all_friendships AS (
    SELECT requester_id as id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id FROM RequestAccepted
)
SELECT id, COUNT(*) as num
FROM all_friendships
GROUP BY id
ORDER BY num DESC
LIMIT 1;

---

## 🧩 Pattern #4: CTEs
* Pattern: CTE for multi-step aggregations

-- Problem: Monthly transaction summaries
-- Pattern: CTE for multi-step aggregations

WITH monthly_stats AS (
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') as month,
        country,
        COUNT(*) as trans_count,
        SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) as approved_count,
        SUM(amount) as trans_total_amount,
        SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) as approved_total_amount
    FROM Transactions
    GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
)
SELECT * FROM monthly_stats;

---

## 🔍 Pattern #5: Subqueries (NOT IN vs NOT EXISTS)

* -- SLOW: NOT IN with subquery (scans entire subquery for each row)
SELECT name
FROM Customers
WHERE id NOT IN (SELECT customer_id FROM Orders);

* -- FAST: NOT EXISTS (short-circuits on first match)
SELECT c.name
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1 FROM Orders o WHERE o.customer_id = c.id
);

* -- FASTEST: LEFT JOIN with NULL check
SELECT c.name
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customer_id
WHERE o.customer_id IS NULL;

---

## 🏝️ Pattern #6: Gap and Islands
* Pattern: ROW_NUMBER() - seat_id grouping technique

-- Problem: Find consecutive available seats
-- Pattern: ROW_NUMBER() - seat_id grouping technique

WITH island_groups AS (
    SELECT 
        seat_id,
        ROW_NUMBER() OVER (ORDER BY seat_id) as rn,
        seat_id - ROW_NUMBER() OVER (ORDER BY seat_id) as island_id
    FROM Cinema
    WHERE free = 1
)
SELECT seat_id
FROM island_groups
GROUP BY island_id
HAVING COUNT(*) >= 2;

---

## 📊 Pattern #7: Pivot Operations
* Pattern: CASE WHEN for manual pivoting

-- Problem: Pivot department revenue by month
-- Pattern: CASE WHEN for manual pivoting

SELECT 
    department,
    SUM(CASE WHEN month = 'Jan' THEN revenue ELSE 0 END) as Jan_Revenue,
    SUM(CASE WHEN month = 'Feb' THEN revenue ELSE 0 END) as Feb_Revenue,
    SUM(CASE WHEN month = 'Mar' THEN revenue ELSE 0 END) as Mar_Revenue
FROM Department
GROUP BY department;

---

## Summary Problem-to-Pattern Cheat Sheet

PROBLEM TYPE                    → PATTERN
══════════════════════════════════════════════════════════
"Top N per group"              → ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)
"Consecutive values"           → LAG/LEAD or island_id technique
"Running totals"               → SUM() OVER (ORDER BY ...)
"Compare to previous"          → LAG(col, 1) OVER (ORDER BY ...)
"Rank with/without gaps"       → RANK() vs DENSE_RANK()
"Hierarchical data"            → Self join or Recursive CTE
"Find missing"                 → NOT EXISTS or LEFT JOIN ... WHERE ... IS NULL
"Pivot/Unpivot"                → CASE WHEN with GROUP BY
"Complex multi-step"           → CTEs for readability
"Statistical calculations"     → Window functions with COUNT/AVG