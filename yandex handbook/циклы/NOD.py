n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
while len(numbers) > 1:
    new_numbers = []
    for i, x in enumerate(numbers):
        if i == numbers.index(min(numbers)):
            new_numbers.append(x)
        elif x % min(numbers) != 0:
            new_numbers.append(x % min(numbers))
    numbers = new_numbers
print(numbers[0])