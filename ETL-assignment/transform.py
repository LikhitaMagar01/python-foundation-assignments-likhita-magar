"""
Pure business-logic functions for the banking ETL pipeline.

No SQL, no psycopg2, no logging side effects here - plain Python data
structures in, plain Python data structures out - so this module can be
imported and unit tested (see test_transform.py) without a database.
"""


def compute_loan_metrics(loans_rows):
    """
    Computes, per customer, total_loan_exposure (sum of principal for
    active loans only), active_loan_count, and a defaulted-loan flag.

    loans_rows: iterable of dicts/rows with keys
                ['customer_id', 'principal', 'status']
    Returns: {customer_id: {"total_loan_exposure": float,
                             "active_loan_count": int,
                             "has_defaulted": bool}}
    """
    metrics = {}
    for row in loans_rows:
        cid = row["customer_id"]
        if cid not in metrics:
            metrics[cid] = {
                "total_loan_exposure": 0.0,
                "active_loan_count": 0,
                "has_defaulted": False,
            }

        status = row["status"]
        if status == "active":
            metrics[cid]["total_loan_exposure"] += float(row["principal"])
            metrics[cid]["active_loan_count"] += 1
        elif status == "defaulted":
            metrics[cid]["has_defaulted"] = True

    return metrics


def categorize_customer(total_amount, has_defaulted_loan=False):
    """
    Categorizes a customer based on loan defaults and transaction totals.
    - Any defaulted loan          => 'At Risk' (overrides everything else)
    - total_amount >= 20000       => 'Premium'
    - total_amount >= 5000        => 'Standard'
    - otherwise                   => 'Basic'
    """
    if has_defaulted_loan:
        return "At Risk"
    if total_amount >= 20000:
        return "Premium"
    if total_amount >= 5000:
        return "Standard"
    return "Basic"


def check_high_value_flag(amount, threshold=10000):
    """Flags a transaction that exceeds the high-value threshold."""
    return amount > threshold
