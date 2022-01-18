class Quadrate:
    def __init__(self, a):
        self.side = a
    def __str__(self):
        return f"Quadrate(side = {self.side})"

class Circle:
    def __init__(self, b):
        self.radius = b
    def __str__(self):
        return f"Circle(radius = {self.radius})"

class Triangle:
    def __init__(self, c, h):
        self.base = c
        self.height = h
    def __str__(self):
        return f"Triangle(base = {self.base}, height = {self.height})"

quad_1 = Quadrate(5)
quad_2 = Quadrate(10)
circle_1 = Circle(7)
circle_2 = Circle(12)
trian_1 = Triangle(6, 4)
trian_2 = Triangle(8, 2)

print(quad_1)
print(quad_2)
print(circle_1)
print(circle_2)
print(trian_1)
print(trian_2)