n = int(input())
d = {}

for _ in range(n):
    sur = input()
    d[sur] = d.get(sur, 0) + 1

print(sum(x for x in d.values() if x > 1))