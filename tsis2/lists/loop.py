thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

[print(x) for x in thislist]