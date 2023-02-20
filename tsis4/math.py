import math

def degree_to_radian(l):
    r = math.pi * l / 180
    return r

h = int(input("Height: "))
b1 = int(input("Base 1: "))
b2 = int(input("Base 2: "))
print((b1 + b2) * .5 * h)

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
x = float(.25 * n * l**2 * (math.cos(degree_to_radian(180 / n)) / math.sin(degree_to_radian(180 / n))))
print("Area of parallelogram: {par_square}".format(par_square=x))

l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print(l * h)