n = int(input())
summary = 0
for _ in range(n):
    summary += sum(int(c) for c in input())
print(summary)
