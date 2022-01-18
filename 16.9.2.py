class Rectangle():
    def __init__(self, a, b):
        self.length = a
        self.width = b
    def rectangle_area(self):
        return self.length * self.width

countRectangle = Rectangle(8, 3)
print("Площадь прямоугольника: ", countRectangle.rectangle_area())