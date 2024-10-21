"""Напишите программу для определения количества простых чисел среди введённых."""

def find_primes_for_largest(x: int) -> list:
    primes = []
    for i in range(2, int(x ** (1 / 2)) + 1):
        for prime in primes:
            if i % prime == 0:
                break
        primes.append(i)
        
    return primes


def is_prime(x: int, primes: list) -> bool:
    for prime in primes:
        if x == prime:
            return True
        if x % prime == 0 or prime > x ** 2:
            return False
    return True
  

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
primes = find_primes_for_largest(max(nums))
count = 0
for num in nums:
    count += is_prime(num, primes)
print(count)