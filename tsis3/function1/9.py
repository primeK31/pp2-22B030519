import math

def volume_sphere(r):
    return (4 / 3) * math.pi * pow(r, 3)


r = int(input())
print(volume_sphere(r))