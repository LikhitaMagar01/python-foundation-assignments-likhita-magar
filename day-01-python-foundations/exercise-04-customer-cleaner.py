"""
Exercise 4: Customer Record Cleaner
Student: Likhita
Day: 1
"""

# input values
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# calculations
clean_name = raw_name.strip().title()
clean_city = raw_city.strip().title()
clean_age = int(raw_age)
clean_email = raw_email.strip().lower()

# function definition
def status(age):
  return 'Adult' if age >= 18 else 'Minor'

# function call
status_value = status(clean_age)

# output
print(f"Name: {clean_name}")
print(f"City: {clean_city}")
print(f"Age: {clean_age}")
print(f"Email: {clean_email}")
print(f"Status: {status_value}")
