def uniq(s):
    l = list()
    for i in s:
        if i not in l:
            l.append(i)
    print(l)


s = input()
s = s.split()
uniq(s)