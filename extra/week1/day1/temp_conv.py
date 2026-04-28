"""
temperature_conversion
--------------------------
Converts a Celsius input to Fahrenheit.

- float(): accepts decimals, raises ValueError on non-numeric input
- while True + try/except: loops until valid input
- :.2f: formats result to 2 decimal places
- \u00b0: unicode for the degree symbol °
"""

while True:
    try:
        c = float(input("Enter the temperature in Celsius: "))
        break
    except ValueError:
        print("Please input numbers")

print(f"{c}\u00b0C = {(c * 9 / 5 + 32):.2f}\u00b0F")