# Printing even numbers from combined list of two

list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 6, 8, 6, 9]

def main():
    n = (list_1 + list_2)
    n = sorted(n)
    # Even numbers only, sorted across both list
    for i in n:
        if i % 2 == 0:
            print(i)


if __name__ == "__main__":
    main()