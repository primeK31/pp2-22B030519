import os

f = open("first.txt", "w")
l = os.listdir(r"D:\python_labs\pp2-22B030519\tsis6")
text = '\n'.join(l)
f.write(text)
f.close()