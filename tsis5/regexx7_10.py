import re

l = list()
txt = input("Seven: ")
c = re.split('_', txt)
for i in c:
    l.append(i.capitalize())
r = "".join(l)
print(r)

txt = input("Eight: ")
c = re.split('[A-Z]', txt)
print(c)

txt = input("Nine: ")
c = re.findall('[A-Z][a-z]*', txt)
r = " ".join(c)
print(r)

txt = input("Ten: ")
l = list()
c = re.findall('[A-Z][a-z]*', txt)
for i in c:
    l.append(i.lower())
r = "_".join(l)
print(r)
