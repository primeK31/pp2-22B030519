def palindr(s):
    if s == s[::-1]:
        return True
    else:
        return False


s = input()
print(palindr(s))