"""
einstein.py
------------------------
Converts mass to energy using Einstein's E = mc².

- float(): accepts decimal mass values in kilograms
- c = 3 * 10**8: speed of light in metres per second (approximation)
- c**2: speed of light squared as per the formula
- :.2e: formats result in scientific notation to 2 decimal places
- J: unit of energy is Joules
"""

m = float(input("M (kg): "))
c = 3 * 10**8
print(f"E: {m * c**2:.2e} J")