import random
import datetime

import temperature_utils
from temperature_utils import celsius_to_fahrenheit

celsius = [random.randint(15, 40) for c in range(5)]
fahrenheit = [celsius_to_fahrenheit(c) for c in celsius]

today = datetime.date.today().strftime("%d-%m-%Y")

print(f"Temperature Report — {today}")
print(f"Celsius:    {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print(f"Module version: {temperature_utils.MODULE_VERSION}")
