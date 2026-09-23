import pytest

from transform import (
    compute_loan_metrics,
    categorize_customer,
    check_high_value_flag,
)

# ---------------------------------------------------------------------
# Task 5: Pytest Unit Tests
#
# These import the real pipeline logic from transform.py (the same
# module the notebook's transform step uses), so passing tests here
# prove the actual pipeline behaves correctly, not a re-implementation.
# ---------------------------------------------------------------------


def test_category_boundaries():
    """Test boundary conditions for transaction-based customer categorization."""
    # Exact boundary for Standard (5000)
    assert categorize_customer(5000.00, has_defaulted_loan=False) == "Standard"
    assert categorize_customer(4999.99, has_defaulted_loan=False) == "Basic"

    # Exact boundary for Premium (20000)
    assert categorize_customer(20000.00, has_defaulted_loan=False) == "Premium"
    assert categorize_customer(19999.99, has_defaulted_loan=False) == "Standard"


def test_defaulted_loan_override():
    """A customer with a defaulted loan must ALWAYS be 'At Risk' regardless of spending."""
    # High-spending customer with default
    assert categorize_customer(50000.00, has_defaulted_loan=True) == "At Risk"
    # Low-spending customer with default
    assert categorize_customer(100.00, has_defaulted_loan=True) == "At Risk"


def test_zero_loans():
    """Customers with zero active loans compute exposure = 0 without raising errors."""
    sample_loans = [
        {"customer_id": 1, "principal": 1000.00, "status": "paid_off"},
        {"customer_id": 1, "principal": 2500.00, "status": "defaulted"},
    ]
    metrics = compute_loan_metrics(sample_loans)
    # Customer 1 has no ACTIVE loans
    assert metrics[1]["total_loan_exposure"] == 0.0
    assert metrics[1]["active_loan_count"] == 0
    assert metrics[1]["has_defaulted"] is True


def test_high_value_flag_logic():
    """Verify that the original high-value transaction flag logic is intact."""
    assert check_high_value_flag(10000.01) is True
    assert check_high_value_flag(10000.00) is False
    assert check_high_value_flag(5000.00) is False


def test_loan_exposure_calculation():
    """Verify exposure correctly sums ALL active loans, not just the first one seen."""
    sample_loans = [
        {"customer_id": 10, "principal": 5000.00, "status": "active"},
        {"customer_id": 10, "principal": 3000.00, "status": "active"},
        {"customer_id": 10, "principal": 2000.00, "status": "paid_off"},
    ]
    metrics = compute_loan_metrics(sample_loans)
    assert metrics[10]["total_loan_exposure"] == 8000.00
    assert metrics[10]["active_loan_count"] == 2


def test_active_loan_after_defaulted_loan_still_counted():
    """
    Regression test: a customer whose FIRST loan row is defaulted must still
    have later ACTIVE loans counted toward exposure (this was broken before -
    the buggy version only ever looked at each customer's first loan row).
    """
    sample_loans = [
        {"customer_id": 3, "principal": 15000.00, "status": "defaulted"},
        {"customer_id": 3, "principal": 3000.00, "status": "active"},
    ]
    metrics = compute_loan_metrics(sample_loans)
    assert metrics[3]["has_defaulted"] is True
    assert metrics[3]["total_loan_exposure"] == 3000.00
    assert metrics[3]["active_loan_count"] == 1
