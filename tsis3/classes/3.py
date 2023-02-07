class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


h = int(input("Height: "))
w = int(input('Width: '))
rectangle = Rectangle(h, w)
print("Area of the rectangle:", rectangle.area())