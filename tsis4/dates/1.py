import datetime

l = datetime.datetime.now()
x = datetime.datetime(l.year, l.month, l.day - 5, l.hour, l.minute, l.second, l.microsecond)

print(x)

l = datetime.datetime.now()
for i in range(-1, 2): # Yesterday, today, tommorow
    print(l.day + i)

l = datetime.datetime.now()
print(l.strftime("%c"))

l = datetime.datetime.now()
r = datetime.datetime.now()

x = l - r
print(x)