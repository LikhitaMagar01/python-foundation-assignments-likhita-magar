"""
Exercise 2: Data Quality Checker
Student: Likhita
Day: 1
"""

# input values
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# calculations
total_problematic_rows = missing_rows + duplicate_rows
total_problematic_rows_rate = total_problematic_rows / total_rows * 100

# output
print(f"Total rows: {total_rows}")
print(f"Total problematic rows: {total_problematic_rows}")
print(f"Total problematic rows rate: {total_problematic_rows_rate:.2f}%")

# function definition
def classification(rate):
  if rate <= 2:
    print('excellent')
  elif rate >= 2 and rate <= 5:
    print('acceptable')
  elif rate >= 5:
    print('needs cleaning')

# function call
classification(total_problematic_rows_rate)
