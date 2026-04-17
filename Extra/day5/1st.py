# Comparison(max, min) and calculation of average

numbers = []
def calc(n):
    low = f"Min = {min(n)}"
    high = f"Max = {max(n)}"
    avg = f"Average = {(sum(n) / len(n)):.2f}"
    return f"{low}\n{high}\n{avg}"

def main():
    # 'for' loop ensures to take only 5 valid input
    for i in range(0,5):
        # 'while' loop ensures invalid input re-promts instead of skipping
        while True:
            try:
                num = float(input("Number: "))
                numbers.append(num)
                break
            except (ValueError):
                print("Please enter a valid number")
    print(calc(numbers), end = "")


if __name__ == "__main__":
    main()
