import time

num = int(input())
m = int(input())

time.sleep(m / 1000)
print("Square root of {number} after {time} miliseconds is {result}".format(number=num, time=m, result=num**.5))
