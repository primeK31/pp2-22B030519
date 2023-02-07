import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point position: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


p1_x = int(input("Point1 x: "))
p1_y = int(input("Point1 y: "))
p2_x = int(input("Point2 x: "))
p2_y = int(input("Point2 y: "))
p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)

p1.show()
p2.show()

print("Distance between two points:", p1.dist(p2))