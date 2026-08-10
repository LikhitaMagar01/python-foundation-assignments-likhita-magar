"""
Exercise 4: Sales List Analysis
Student: Likhita
Day: 2
"""

# input values
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]
above_100000 = []

# calculations
# 1
sorted_list = sorted(monthly_sales, reverse=True)

# 2
for sales in monthly_sales:
  if sales > 100000:
    above_100000.append(sales)

# 3
total_sales = sum(monthly_sales)
total_sales_with_vat = [ x + (13 / 100 * x) for x in monthly_sales ]

# 4
total_sales = sum(monthly_sales)

# 5
avg_sales_amount = total_sales / len(monthly_sales)

# output
print(f"sorted list: {sorted_list}")
print(f"list above 100000:  {above_100000}")
print(f"list with 13% vat: {total_sales_with_vat}")
print(f"total sales amount: {total_sales}")
print(avg_sales_amount)
