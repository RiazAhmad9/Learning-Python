# Temp convert calc.

# 'main' function where user get to choose between c and f and print the final result considering there provided value.
def main():
    choice = input("C or F: ").lower().strip()
    if choice == "c":
        n = float(input("C: ").strip())
        print(f"F: {c_to_f(n):.2f}\u00b0")
    elif choice == "f":
        n = float(input("F: ").strip()) 
        print(f"C: {f_to_c(n):.2f}\u00b0")

# 'c_to_f' function where celsius get converted into fahrenheit.
def c_to_f(f):
    f = ((f * (9/5)) + 32)
    return f

# 'f_to_c' function where fahrenheit gets converted into celsius.
def f_to_c(c):
    c = ((c - 32) * (5/9))
    return c

# Calls main.
main()
