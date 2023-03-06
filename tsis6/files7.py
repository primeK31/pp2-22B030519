import os

l = list
with open(r"orig.txt", 'r') as f:
    l = list(f)
f = open(r"orig_clown.txt", 'w')
text = '\n'.join(l)
f.write(text)
f.close()
