# super() = function that is used in child class to call methods from a parent class(superclass)
# allows you to extend the functionality of the inherited methods

class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def description(self):
        print(f"It is {self.color} color, and is {'filled' if self.is_filled else 'not filled' }")

class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        
        self.radius = radius

    def description(self):
        print(f"It's area is {3.14 * self.radius**2}")
        super().description()


class Square(Shapes):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


class Triangle(Shapes):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle("Blue", True, 5)
square = Square("Purple", False, 25)
triangle = Triangle("Yellow", True, 45, 32)

print(circle.radius)
print(circle.color)
print(square.is_filled)
print(triangle.color)
circle.description()

