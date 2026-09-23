# Assignment 5: Robust Banking ETL Pipeline

This project extends the class ETL pipeline (Postgres + `psycopg2`) to track
customer loans, harden the connection against transient failures, update the
categorization business logic, and verify correctness with a reconciliation
report and unit tests.

## Schema Extension

1. **`loans` table** — new, linked to `customers` via a `customer_id` foreign
   key (`ON DELETE CASCADE`). Columns: `loan_id`, `customer_id`, `principal`,
   `interest_rate`, `start_date`, and `status` constrained by
   `CHECK (status IN ('active', 'paid_off', 'defaulted'))`.
2. **`account_summary` table** — extended with two columns:
   `total_loan_exposure NUMERIC(12,2)` (sum of principal across active loans
   only) and `active_loan_count INTEGER`.

All DDL uses `CREATE TABLE IF NOT EXISTS`, and all seed/upsert statements use
`ON CONFLICT`, so `create_schema` and `seed_data` are safe to re-run.

## Business logic (`transform.py`)

The pure transformation functions — `compute_loan_metrics`,
`categorize_customer`, `check_high_value_flag` — live in `transform.py`,
separate from the notebook and from any SQL. The notebook imports them for
the real pipeline, and `test_transform.py` imports the same module, so the
unit tests exercise the actual pipeline logic rather than a copy of it.

Categorization rules:
- Any loan with `status = 'defaulted'` → always **At Risk**, regardless of
  transaction total.
- Otherwise: `>= 20000` → **Premium**, `>= 5000` → **Standard**, else
  **Basic**.

## Connection hardening (Task 2)

`DBConnection.execute_query` is wrapped by the `retry_db_operation` decorator,
which retries up to 3 times on `psycopg2.OperationalError`, sleeping briefly
between attempts, and logs each attempt to `etl.log`. It also rolls back the
connection before retrying **when a connection was actually established** —
if `psycopg2.connect()` itself fails (e.g. the server is unreachable), there
is no live transaction to roll back, so rollback is skipped by design in that
case; it fires when a query fails mid-transaction on an open connection.

The notebook's Task 2 demo (cell 5, step 4) points a second `DBConnection` at
an unreachable port to trigger a real `OperationalError`, showing 3 logged
retry attempts followed by the error being re-raised and handled — visible in
`etl.log`.

## Setup and running

**Prerequisites:** Python 3.10+, a running PostgreSQL instance, and the
`psycopg2`, `python-dotenv`, and `pytest` packages installed.

**Environment variables** — copy `.env.example` to `.env` (not committed) and
fill in real values:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bank_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

The notebook calls `load_dotenv()` before reading these, with safe
placeholder defaults in code (never real credentials).

**Run the pipeline:**

```
jupyter nbconvert --to notebook --execute --inplace Assignment_ETL.ipynb
```

or open `Assignment_ETL.ipynb` in Jupyter and run all cells top to bottom.
This creates/verifies the schema, seeds sample data, runs extract → transform
→ load, prints a reconciliation report, and demonstrates the retry/rollback
behavior. Logs are written to `etl.log`.

**Run the unit tests:**

```
pytest test_transform.py -v
```
