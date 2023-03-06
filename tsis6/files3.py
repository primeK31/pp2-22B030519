import os

dr = input()
print(os.path.isdir(dr))
l = os.listdir(dr)
text = '\n'.join(l)
print(text)
