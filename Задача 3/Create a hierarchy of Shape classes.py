from math import pi, sqrt

# 基础形状类Базовый класс формы
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def compare_area(self, other):
        if self.area() > other.area():
            return "The first shape has a larger area"
        elif self.area() < other.area():
            return "The first shape has a smaller area"
        else:
            return "The areas of two shapes are equal"
    
    def compare_perimeter(self, other):
        if self.perimeter() > other.perimeter():
            return "The first shape has a longer perimetere"
        elif self.perimeter() < other.perimeter():
            return "The first shape has a shorter perimeter"
        else:
            return "The perimeters of the two shapes are equal"

# 正方形类класс квадрата
class Square(Shape):
    def __init__(self, sideLength):
        self.sideLength = sideLength
    
    def area(self):
        return self.sideLength** 2
    
    def perimeter(self):
        return 4 * self.sideLength

# 矩形类класс прямоугольника
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# 三角形类класс треугольника
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        p = (self.side1 + self.side2 + self.side3)/2

        #海伦公式计算三角形面积Формула Герона вычисляет площадь треугольника
        return sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# 圆形类класс круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self.radius
    

# 示例使用Например:
mySquare = Square(6)
myRectangle = Rectangle(1, 11)
myTriangle = Triangle(3, 4, 4)
myCircle = Circle(3)

print(f"Square area: {mySquare.area()}")
print(f"Circle perimeter: {myCircle.perimeter()}")
print(f"Square vs Rectangle perimeter: {mySquare.compare_perimeter(myRectangle)}")
