import re

txt = input("Fourth: ")
pattern = r'[A-Z][a-z]+'
r = re.findall(pattern, txt)
print(r)

txt = input("Fifth: ")
pattern = r'a(.)*(b)'
if r:
    print("True")
else:
    print("No matches")

txt = input("Sixth: ")
pattern = '[ ,.]'
r = re.sub(pattern, ":", txt)
print(r)