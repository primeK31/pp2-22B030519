def filter_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = list()
for i in range(100):
    n.append(i)
prime_numbers = list(filter(lambda x: filter_prime(x), n))
print("Prime numbers in the list:", prime_numbers)