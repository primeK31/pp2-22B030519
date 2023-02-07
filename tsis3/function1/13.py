import random


def guess_number(name):
    print(f"Well, {name}, I am thinking of a number between 1 and 20. ")
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
            print(f"Good job, {name}! You guessed my number in {c} guesses!")
            break


name = input("Hello! What is your name? ")
guess_number(name)