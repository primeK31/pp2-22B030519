def multik(l):
    c = 1
    for i in l:
        c *= i
    return c


l = [1, 2, 3, 4, 5]
print(multik(l), end=" ")
