"""
Exercise 3: File Validator
Student: Likhita
Day: 1
"""

# input values
user_input = input("Enter your file")

# variables
file_name = user_input.strip().lower()
allowed_extension = ('csv', 'json', 'parquet')

# function definition
def fileValidation(file):
  if file.endswith(allowed_extension):
    print(f"{file} is a valid file.")
    return
  print(f"{file} is not a valid file")

# function call
fileValidation(file_name)
