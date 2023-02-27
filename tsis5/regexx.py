import re

txt = input("First: ")
pattern = r'ab*'
r = re.search(pattern, txt)
if r:
    print("True")
else:
    print("No match")

txt = input("Second: ")
pattern = r'a(b){2-3}'
r = re.search(pattern, txt)
if r:
    print("True")
else:
    print("No match")

txt = input("Third: ")
pattern = r'[a-z]+_[a-z]+'
r = re.findall(pattern, txt)
print(r)