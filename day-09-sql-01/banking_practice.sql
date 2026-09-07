DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS accounts     CASCADE;
DROP TABLE IF EXISTS customers    CASCADE;

CREATE TABLE customers (
    customer_id   int PRIMARY KEY,
    first_name    varchar(50),
    last_name     varchar(50),
    gender        varchar(50),
    dob           date,
    city          varchar(50),
    state         varchar(50),
    country       varchar(50),
    phone         varchar(50),
    email         varchar(50),
    occupation    varchar(50),
    annual_income numeric(14,2),
    credit_score  int,
    kyc_status    varchar(20),
    join_date     date,
    risk_category varchar(20)
);

CREATE TABLE accounts (
    account_id       int PRIMARY KEY,
    customer_id      int NOT NULL,
    account_type     varchar(30),
    branch           varchar(50),
    ifsc_code        varchar(15),
    currency         varchar(5),
    balance          numeric(14,2),
    interest_rate    numeric(5,2),
    open_date        date,
    close_date       date,
    status           varchar(20),
    is_joint_account boolean
);

CREATE TABLE transactions (
    transaction_id int PRIMARY KEY,
    account_id     int NOT NULL,
    txn_date       date,
    txn_time       time,
    txn_type       varchar(30),
    channel        varchar(30),
    amount         numeric(14,2),
    currency       varchar(5),
    balance_after  numeric(14,2),
    merchant       varchar(60),
    description    varchar(100),
    is_flagged     boolean
);

-- 1. Show every ACTIVE account together with the owning customer's full name and email. Only Active accounts should appear.
SELECT a.account_id, a.account_type, a.branch, a.balance,
       c.first_name || ' ' || c.last_name AS full_name, c.email
FROM accounts a
JOIN customers c ON c.customer_id = a.customer_id
WHERE a.status = 'Active'
ORDER BY a.account_id;

-- 2. Find every customer who currently has NO account at all.
SELECT c.customer_id, c.first_name || ' ' || c.last_name AS full_name
FROM customers c
LEFT JOIN accounts a ON a.customer_id = c.customer_id
WHERE a.account_id IS NULL
ORDER BY c.customer_id;

-- 3. Find every account whose customer_id does not match any row in the customers table (orphaned accounts).
SELECT a.account_id, a.customer_id, a.branch, a.balance
FROM accounts a
WHERE NOT EXISTS (
    SELECT 1 FROM customers c WHERE c.customer_id = a.customer_id
);

-- 4. Produce one result set of every customer and every account regardless of whether a match exists on either side, and label each row as 'Matched', 'No Account' or 'Missing Customer'.
SELECT c.customer_id, a.account_id,
       CASE WHEN c.customer_id IS NOT NULL AND a.account_id IS NOT NULL
                 THEN 'Matched'
            WHEN a.account_id IS NULL THEN 'No Account'
            ELSE 'Missing Customer'
       END AS match_status
FROM customers c
FULL OUTER JOIN accounts a ON a.customer_id = c.customer_id
ORDER BY match_status, c.customer_id;

-- 5. For every transaction, show the transaction id, amount, account type, branch and the owning customer's full name - a single query joining three tables.
SELECT t.transaction_id, t.amount, a.account_type, a.branch,
       c.first_name || ' ' || c.last_name AS full_name
FROM transactions t
JOIN accounts  a ON a.account_id  = t.account_id
JOIN customers c ON c.customer_id = a.customer_id
ORDER BY t.transaction_id;

-- 6. Find the total balance held at each branch, ordered from highest to lowest.
SELECT branch, SUM(balance) AS total_balance
FROM accounts
GROUP BY branch
ORDER BY total_balance DESC;

-- 7. Find the TOP 5 branches by total balance, counting only Active accounts.
SELECT branch, SUM(balance) AS total_balance, COUNT(*) AS active_accounts
FROM accounts
WHERE status = 'Active'
GROUP BY branch
ORDER BY total_balance DESC
LIMIT 5;

-- 8. Find account types where the average balance exceeds 50,000. Round the average to 2 decimal places.
SELECT account_type, ROUND(AVG(balance), 2) AS avg_balance
FROM accounts
GROUP BY account_type
HAVING AVG(balance) > 50000
ORDER BY avg_balance DESC;

-- 9. Count how many accounts each customer holds, and list only customers who hold more than 1 account.
SELECT c.customer_id,
       c.first_name || ' ' || c.last_name AS full_name,
       COUNT(a.account_id) AS account_count
FROM customers c
JOIN accounts a ON a.customer_id = c.customer_id
GROUP BY c.customer_id, full_name
HAVING COUNT(a.account_id) > 1
ORDER BY account_count DESC;

-- 10. Find the branch and account_type combination that has the single highest total transaction amount.
SELECT a.branch, a.account_type, SUM(t.amount) AS total_txn_amount
FROM transactions t
JOIN accounts a ON a.account_id = t.account_id
GROUP BY a.branch, a.account_type
ORDER BY total_txn_amount DESC
LIMIT 1;

-- 11. Find every customer whose COMBINED account balance is greater than the overall average balance across all accounts.
SELECT c.customer_id,
       c.first_name || ' ' || c.last_name AS full_name,
       SUM(a.balance) AS total_balance
FROM customers c
JOIN accounts a ON a.customer_id = c.customer_id
GROUP BY c.customer_id, full_name
HAVING SUM(a.balance) > (SELECT AVG(balance) FROM accounts)
ORDER BY total_balance DESC;

-- 12. Find accounts whose balance is above the average balance of their own account_type (correlated subquery).
SELECT a.account_id, a.account_type, a.balance
FROM accounts a
WHERE a.balance > (
    SELECT AVG(a2.balance)
    FROM accounts a2
    WHERE a2.account_type = a.account_type
)
ORDER BY a.account_id;

-- 13. Using EXISTS, find every customer who has made at least one 'Withdrawal' transaction.
SELECT c.customer_id, c.first_name || ' ' || c.last_name AS full_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM accounts a
    JOIN transactions t ON t.account_id = a.account_id
    WHERE a.customer_id = c.customer_id
      AND t.txn_type = 'Withdrawal'
)
ORDER BY c.customer_id;

-- 14. Using NOT EXISTS, find every account that has never had a single transaction.
SELECT a.account_id, a.account_type, a.branch, a.balance
FROM accounts a
WHERE NOT EXISTS (
    SELECT 1 FROM transactions t WHERE t.account_id = a.account_id
)
ORDER BY a.account_id;

-- 15. Using IN with a subquery, list customers who live in a city that has more than 3 customers.
SELECT customer_id, first_name || ' ' || last_name AS full_name, city
FROM customers
WHERE city IN (
    SELECT city
    FROM customers
    WHERE COALESCE(city, '') <> ''
    GROUP BY city
    HAVING COUNT(*) > 3
)
ORDER BY city, customer_id;

-- 16. Using a subquery in the FROM clause (inline view), compute the number of accounts and average balance per branch, then keep only branches with more than 5 accounts.
SELECT *
FROM (
    SELECT branch,
           COUNT(*) AS account_count,
           ROUND(AVG(balance), 2) AS avg_balance
    FROM accounts
    GROUP BY branch
) b
WHERE b.account_count > 5
ORDER BY b.account_count DESC;

-- 17. Combine the customer ids that hold a Savings account with the customer ids that hold a Checking account into ONE de-duplicated list, using UNION.
SELECT customer_id FROM accounts WHERE account_type = 'Savings'
UNION
SELECT customer_id FROM accounts WHERE account_type = 'Checking'
ORDER BY customer_id;

-- 18. Produce the same combined Savings/Checking customer list but KEEP duplicates (a customer with both types should appear twice), using UNION ALL.
SELECT customer_id FROM accounts WHERE account_type = 'Savings'
UNION ALL
SELECT customer_id FROM accounts WHERE account_type = 'Checking'
ORDER BY customer_id;

-- 19. Find customer ids that appear in BOTH the Savings list and the Checking list, using INTERSECT.
SELECT customer_id FROM accounts WHERE account_type = 'Savings'
INTERSECT
SELECT customer_id FROM accounts WHERE account_type = 'Checking'
ORDER BY customer_id;

-- 20. Find customer ids that have a Savings account but do NOT have a Fixed Deposit account, using EXCEPT.
SELECT customer_id FROM accounts WHERE account_type = 'Savings'
EXCEPT
SELECT customer_id FROM accounts WHERE account_type = 'Fixed Deposit'
ORDER BY customer_id;

-- 21.Write a CTE that calculates each account's total transaction amount, then use it to list only accounts whose total exceeds 100,000.
WITH account_totals AS (
    SELECT account_id, SUM(amount) AS total_amount
    FROM transactions
    GROUP BY account_id
)
SELECT a.account_id, a.account_type, a.branch, t.total_amount
FROM account_totals t
JOIN accounts a ON a.account_id = t.account_id
WHERE t.total_amount > 100000
ORDER BY t.total_amount DESC;

-- 22. Write a CTE to find the single highest-balance account in EACH branch.
WITH ranked AS (
    SELECT a.*,
           ROW_NUMBER() OVER (PARTITION BY branch ORDER BY balance DESC) AS rn
    FROM accounts a
)
SELECT branch, account_id, account_type, balance
FROM ranked
WHERE rn = 1
ORDER BY balance DESC;

-- 23. Chain two CTEs together: the first totals Deposit transactions per account, the second joins that total to accounts and returns accounts whose total deposits exceed their current balance.
WITH deposit_totals AS (
    SELECT account_id, SUM(amount) AS total_deposits
    FROM transactions
    WHERE txn_type = 'Deposit'
    GROUP BY account_id
),
flagged AS (
    SELECT a.account_id, a.branch, a.balance, d.total_deposits
    FROM deposit_totals d
    JOIN accounts a ON a.account_id = d.account_id
    WHERE d.total_deposits > a.balance
)
SELECT * FROM flagged
ORDER BY total_deposits DESC;

-- 24.Create a VIEW named active_accounts_view exposing only Active accounts along with the owning customer's full name.
CREATE OR REPLACE VIEW active_accounts_view AS
SELECT a.account_id, a.account_type, a.branch, a.balance, a.open_date,
       c.customer_id,
       c.first_name || ' ' || c.last_name AS full_name,
       c.email
FROM accounts a
JOIN customers c ON c.customer_id = a.customer_id
WHERE a.status = 'Active';

SELECT * FROM active_accounts_view ORDER BY account_id;

-- 25. Create a MATERIALIZED VIEW named branch_balance_summary that pre-aggregates total balance and account count per branch, and write the command to refresh it CONCURRENTLY.

DROP MATERIALIZED VIEW IF EXISTS branch_balance_summary;

CREATE MATERIALIZED VIEW branch_balance_summary AS
SELECT branch,
       SUM(balance) AS total_balance,
       COUNT(*)     AS account_count
FROM accounts
GROUP BY branch;


CREATE UNIQUE INDEX branch_balance_summary_branch_idx
    ON branch_balance_summary (branch);

REFRESH MATERIALIZED VIEW CONCURRENTLY branch_balance_summary;

SELECT * FROM branch_balance_summary ORDER BY total_balance DESC;

-- 26. Using ROW_NUMBER(), return only the MOST RECENT transaction for every account.
WITH ranked AS (
    SELECT t.*,
           ROW_NUMBER() OVER (
               PARTITION BY account_id
               ORDER BY txn_date DESC, txn_time DESC, transaction_id DESC
           ) AS rn
    FROM transactions t
)
SELECT transaction_id, account_id, txn_date, txn_time, txn_type, amount
FROM ranked
WHERE rn = 1
ORDER BY account_id;

-- 27. Using RANK(), rank customers by their total account balance so that tied balances share the same rank (with a gap afterward).
SELECT c.customer_id,
       c.first_name || ' ' || c.last_name AS full_name,
       SUM(a.balance) AS total_balance,
       RANK() OVER (ORDER BY SUM(a.balance) DESC) AS balance_rank
FROM customers c
JOIN accounts a ON a.customer_id = c.customer_id
GROUP BY c.customer_id, full_name
ORDER BY balance_rank;

-- 28. Using DENSE_RANK(), rank branches by total transaction amount with NO gaps in the ranking numbers.
SELECT a.branch,
       SUM(t.amount) AS total_txn_amount,
       DENSE_RANK() OVER (ORDER BY SUM(t.amount) DESC) AS branch_rank
FROM transactions t
JOIN accounts a ON a.account_id = t.account_id
GROUP BY a.branch
ORDER BY branch_rank;

-- 29. Using LAG(), show each transaction next to the amount of the PREVIOUS transaction on the same account, ordered by date.
SELECT transaction_id, account_id, txn_date, amount,
       LAG(amount) OVER (
           PARTITION BY account_id
           ORDER BY txn_date, txn_time, transaction_id
       ) AS prev_amount
FROM transactions
ORDER BY account_id, txn_date, txn_time;

-- 30. Using LEAD(), show each transaction next to the amount of the NEXT transaction on the same account, and calculate the difference between them.
SELECT transaction_id, account_id, txn_date, amount,
       LEAD(amount) OVER w AS next_amount,
       LEAD(amount) OVER w - amount AS diff
FROM transactions
WINDOW w AS (
    PARTITION BY account_id
    ORDER BY txn_date, txn_time, transaction_id
)
ORDER BY account_id, txn_date, txn_time;

-- 31. Using a running-total window function, show every account's transactions in date order with a cumulative (running) amount.
SELECT transaction_id, account_id, txn_date, amount,
       SUM(amount) OVER (
           PARTITION BY account_id
           ORDER BY txn_date, txn_time, transaction_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM transactions
ORDER BY account_id, txn_date, txn_time;

-- 32. Find duplicate customer records - customers who share the exact same first_name, last_name and dob.
SELECT first_name, last_name, dob,
       COUNT(*) AS dup_count,
       STRING_AGG(customer_id::text, ', ' ORDER BY customer_id) AS ids
FROM customers
GROUP BY first_name, last_name, dob
HAVING COUNT(*) > 1;

-- 33 Write ONE query that finds customers missing a city or email (NULL or blank), and a SECOND query that finds orphaned accounts (customer_id with no matching customer row).
-- 33a. Customers missing a city or email (NULL or blank).
SELECT customer_id, first_name || ' ' || last_name AS full_name, city, email
FROM customers
WHERE city  IS NULL OR TRIM(city)  = ''
   OR email IS NULL OR TRIM(email) = '';

-- 33b. Orphaned accounts.
SELECT a.account_id, a.customer_id
FROM accounts a
WHERE NOT EXISTS (
    SELECT 1 FROM customers c WHERE c.customer_id = a.customer_id
);

-- 34. Using CASE WHEN, bucket every Active account into 'Low' (< 10,000), 'Medium' (10,000-100,000) or 'High' (> 100,000), then count accounts in each bucket.
SELECT CASE WHEN balance < 10000   THEN 'Low'
            WHEN balance <= 100000 THEN 'Medium'
            ELSE 'High'
       END AS balance_bucket,
       COUNT(*) AS account_count
FROM accounts
WHERE status = 'Active'
GROUP BY balance_bucket
ORDER BY account_count DESC;

-- 35. Write a SAFE transaction block that deducts a 500 maintenance fee from every account with balance > 200,000, inserts a matching 'Fee' row into transactions for each of those accounts, and can be rolled back if anything fails. Always filter UPDATE/DELETE with WHERE.
BEGIN;

UPDATE accounts
SET    balance = balance - 500
WHERE  balance > 200000         
  AND  status  = 'Active';

INSERT INTO transactions (
    transaction_id, account_id, txn_date, txn_time, txn_type, channel,
    amount, currency, balance_after, merchant, description, is_flagged)
SELECT (SELECT MAX(transaction_id) FROM transactions)
           + ROW_NUMBER() OVER (ORDER BY account_id),
       account_id, CURRENT_DATE, CURRENT_TIME::time, 'Fee', 'System',
       500, currency, balance, '', 'Monthly maintenance fee', FALSE
FROM   accounts
WHERE  balance > 199500       
  AND  status  = 'Active';

SELECT COUNT(*) AS fee_rows FROM transactions WHERE txn_date = CURRENT_DATE;

ROLLBACK;  

-- 36. Using NTILE(4), split customers into 4 equal-sized income quartiles ordered by annual_income, then count how many customers fall in each quartile.
WITH quartiles AS (
    SELECT customer_id, annual_income,
           NTILE(4) OVER (ORDER BY annual_income) AS income_quartile
    FROM customers
)
SELECT income_quartile,
       COUNT(*)           AS customer_count,
       MIN(annual_income) AS min_income,
       MAX(annual_income) AS max_income
FROM quartiles
GROUP BY income_quartile
ORDER BY income_quartile;

-- 37. Find every customer with a credit_score below 500 who still holds at least one account with a balance above 200,000.
SELECT DISTINCT c.customer_id,
       c.first_name || ' ' || c.last_name AS full_name,
       c.credit_score
FROM customers c
JOIN accounts a ON a.customer_id = c.customer_id
WHERE c.credit_score < 500
  AND a.balance     > 200000
ORDER BY c.credit_score;

-- 38. List every FLAGGED transaction (is_flagged = true) together with the owning customer's name, the branch and the channel used, ordered by amount descending.
SELECT t.transaction_id,
       c.first_name || ' ' || c.last_name AS full_name,
       a.branch, t.channel, t.amount
FROM transactions t
JOIN accounts  a ON a.account_id  = t.account_id
JOIN customers c ON c.customer_id = a.customer_id
WHERE t.is_flagged = TRUE
ORDER BY t.amount DESC;

-- 39. Find every customer whose kyc_status is 'Expired' but who still has at least one 'Active' account (a compliance risk).
SELECT DISTINCT c.customer_id,
       c.first_name || ' ' || c.last_name AS full_name,
       c.kyc_status
FROM customers c
JOIN accounts a ON a.customer_id = c.customer_id
WHERE c.kyc_status = 'Expired'
  AND a.status     = 'Active'
ORDER BY c.customer_id;

-- 40. Find joint accounts (is_joint_account = true) whose balance is above the AVERAGE balance of all accounts in their own branch (correlated subquery).
SELECT a.account_id, a.branch, a.balance
FROM accounts a
WHERE a.is_joint_account = TRUE
  AND a.balance > (
      SELECT AVG(a2.balance)
      FROM accounts a2
      WHERE a2.branch = a.branch
  )
ORDER BY a.balance DESC;




























