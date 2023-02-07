def filter_prime(nums):
    for i in range(len(nums)):
        isPrime = True
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                isPrime = False
        if isPrime:
            print(nums[i])


nums = input()
num = nums.split(' ')
n = [int(x) for x in num]
filter_prime(n)