import random
import math
from itertools import permutations


def grams_to_ounces(grams):
    return 28.3495231 * grams


def fahrenheit_to_centigrade(f):
    return (5 / 9) * (f - 32)


def solve(numheads, numlegs):
    chicken = (numlegs - 2 * numheads) / 2
    rabbit = numheads - chicken
    return chicken, rabbit


def filter_prime(nums):
    for i in range(len(nums)):
        isPrime = True
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                isPrime = False
        if isPrime:
            print(nums[i])


def permut(s):
    l = list(permutations(s))
    for i in l:
        print(''.join(i))


def revers(s):
    r = list(s.split())
    print(" ".join(reversed(r)))


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def spy_game(nums):
    l = list()
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            l.append(nums[i])
    for i in range(len(l) - 2):
        if l[i] == 0 and l[i + 1] == 0 and l[i + 2] == 7:
            return True
    return False


def volume_sphere(r):
    return (4 / 3) * math.pi * pow(r, 3)


def uniq(s):
    l = list()
    for i in s:
        if i not in l:
            l.append(i)
    print(l)


def palindr(s):
    if s == s[::-1]:
        return True
    else:
        return False


def histgrm(l):
    for i in range(len(l)):
        s = list()
        for j in range(l[i]):
            s.append('*')
        print(''.join(s))


def guess_number(name):
    print("Well, {name}, I am thinking of a number between 1 and 20. ".format(name=name))
    n = random.randint(1, 20)
    c = 0
    while True:
        num = int(input("Take guess. "))
        if num > n:
            print("Number is too low.")
            c += 1
        elif num < n:
            print("Number is too big. ")
            c += 1
        elif num == n:
            c += 1
            print("Good job, {name}! You guessed my number in {c} guesses!".format(name=name, c=c))
            break