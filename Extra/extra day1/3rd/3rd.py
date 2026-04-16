# Temperature Conversion (C to F)

# Stores the temperature(C)
c = float(input("Enter the temperature in Celsius: "))

# Prints the converted temperature(F) and 'u00b0' adds a degree sign
print(f"{c}\u00b0C = {c * 9 / 5 + 32}\u00b0F")
