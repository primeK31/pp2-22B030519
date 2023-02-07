def histgrm(l):
    for i in range(len(l)):
        s = list()
        for j in range(l[i]):
            s.append('*')
        print(''.join(s))


l = [4, 9, 7]
histgrm(l)