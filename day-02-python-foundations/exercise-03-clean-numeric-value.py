"""
Exercise 3: Clean Numeric Values
Student: Likhita
Day: 2
"""

# input values
raw_values = [100, None, 250, "invalid", 300, None, 450]
cleaned_values = []

# loop
for value in raw_values:
  if value is not None and isinstance(value, (int, float)):
    cleaned_values.append(value)

# output
print(cleaned_values)
