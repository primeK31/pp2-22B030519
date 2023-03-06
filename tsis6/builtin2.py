def case_num(s):
    up, lol = 0, 0
    for i in s:
        j = ord(i)
        if j >= 65 and j <= 90:
            up += 1
        elif j >= 97 and j <= 122:
            lol += 1
    return (up, lol)


s = "NzmLvEeeeeEo"
upper_case_number, lower_case_number = case_num(s)
print(upper_case_number)
print(lower_case_number)
