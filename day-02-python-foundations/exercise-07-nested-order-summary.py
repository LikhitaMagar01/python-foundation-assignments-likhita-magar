"""
Exercise 7: Nested Order Summary
Student: Likhita
Day: 2
"""

# input values
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# calculations and their outputs
# 1
for order_id, order_details in orders.items():
  print(f"{order_id}: {order_details['customer']}")

# 2
completed_orders = { order_id: order_details for order_id, order_details in orders.items() if order_details['status'] == 'Completed' }
print(f"completed orders are {completed_orders}")

# 3
total_amount_completed = sum(order['amount'] for order in completed_orders.values())
print(f"total amount of completed orders: {total_amount_completed}")

# 4
pending_orders = sum(1 for order in orders.values() if order['status'] == 'Pending')
print(f"number of pending orders: {pending_orders}")

# 5
new_order = {
    "ORD-004": {
        "customer": "likhita",
        "amount": 4000,
        "status": "Pending"
    }
}
orders.update(new_order)
print(f"updated orders: {orders}")
