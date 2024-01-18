# Parent class
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def display(self):
        print(f"Color: {self.color}")

# Child class inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Child class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def display(self):
        super().display()
        print(f"Length: {self.length}, Breadth: {self.breadth}")

# Main program
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 2, 4)

circle.display()
print("Area:", circle.area())

print()

rectangle.display()
print("Area:", rectangle.area())