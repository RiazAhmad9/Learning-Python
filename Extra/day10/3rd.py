# Validateing a birth year

while True:
    try:
        year = int(input("Birth year: "))
        if 1900 < year <= 2026:
            break
        else:
            print("Enter a valid birth year(1900-2026)")
    except ValueError:
        print("Input whole numbers")