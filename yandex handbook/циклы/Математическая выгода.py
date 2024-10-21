n = int(input())
ind = 0
maximum = 0
for i in range(2, 11):
    summary = 0
    b = n % i
    a = n // i
    summary += b
    while a != 0:
        b = a % i
        a = a // i
        summary += b
    if summary > maximum:
        ind = i
        maximum = summary
print(ind)