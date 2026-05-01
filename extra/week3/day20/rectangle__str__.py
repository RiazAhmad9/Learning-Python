"""
Rectangle Class — OOP Fundamentals __str__
===================================
Demonstrates a basic class with attributes and methods.

Class:
    Rectangle(width, height)

    Attributes:
        width  (float) — width of the rectangle
        height (float) — height of the rectangle

    Methods:
        area()      → returns width * height
        perimeter() → returns 2 * (width + height)
        is_square() → returns True if width == height
        __str__()   →  returns square status, area, and perimeter

main():
    Prompts user for width and height (positive floats only),
    prints 'rectangle'
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width +self.height)
    
    def is_square(self):
        return self.width == self.height
    
    def __str__(self):
        square = "Yes" if self.is_square() else "No"
        return f"Square: {square}\nArea: {self.area()}\nPerimeter: {self.perimeter()}"


def main():
    while True:
        try:
            width = float(input("Width: "))
            height = float(input("Height: "))
            if width <= 0 or height <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter only positive numbers")
    rectangle = Rectangle(width, height)
    print(rectangle)

if __name__ == "__main__":
    main()