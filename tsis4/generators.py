import math

def square_generator(n):
    for i in range(1, n + 1):
        if math.sqrt(i) == int(math.sqrt(i)):
            yield i


def even_generator(n):
    for i in range(2, n + 1):
        if i % 2 == 0:
            yield i


def three_and_four(n):
    for i in range(1, n + 1):
        if i % 12 == 0:
            yield i


def squares(a, b):
    for i in range(a, b + 1):
        yield i**2


def revrs(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Input n: "))
x = square_generator(n)
x1 = even_generator(n)
l = list()
for i in x:
    print(i)
for i in x1:
    l.append(i)
print(*l, sep=", ")
n = int(input("Input n: "))
t = three_and_four(n)
for i in t:
    print(i)
a = int(input("Input a: "))
b = int(input("Input b: "))
s = squares(a, b)
for i in s:
    print(i)
n = int(input("n tupnI: "))
r = revrs(n)
l1 = list()
for i in r:
    l1.append(i)
print(*l1, sep=", ")
