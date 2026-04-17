# Temp convert system

# 'main' function which provide user with a option, stores value and prints the final result
def main():
    choice = input("Please choose (C/F): ").lower().strip()
    if choice == "c":
        n = float(input("C: ").strip())
        print(f"F: {c_to_f(n):.2f}\u00b0")
    elif choice == "f":
        n = float(input("F: ").strip()) 
        print(f"C: {f_to_c(n):.2f}\u00b0")

# 'c_to_f' function where celsius get converted into fahrenheit
def c_to_f(f):
    f = ((f * (9/5)) + 32)
    return f

# 'f_to_c' function where fahrenheit gets converted into celsius
def f_to_c(c):
    c = ((c - 32) * (5/9))
    return c

# Calls main
main()
