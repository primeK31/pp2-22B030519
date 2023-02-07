def spy_game(nums):
    l = list()
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            l.append(nums[i])
    for i in range(len(l) - 2):
        if l[i] == 0 and l[i + 1] == 0 and l[i + 2] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5])) # --> True
print(spy_game([1,0,2,4,0,5,7])) # --> True
print(spy_game([1,7,2,0,4,5,0])) # --> False