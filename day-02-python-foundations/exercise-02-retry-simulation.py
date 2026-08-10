"""
Exercise 2: Retry Simulation
Student: Likhita
Day: 2
"""

# variables
attempt = 1
max_attempts = 3
operation_successful = False

# loop
while attempt <= max_attempts:
  print(f"Attempt {attempt}")
  if attempt == 2:
    operation_successful = True
    break

  attempt += 1

# output
if operation_successful:
  print("Operation completed successfully")
else:
  print("Operation failed")
