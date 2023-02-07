from itertools import permutations

def permut(s):
    l = list(permutations(s))
    for i in l:
        print(''.join(i))


s = input()
permut(s)