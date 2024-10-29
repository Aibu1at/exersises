n = int(input())
m = int(input())
kash = set()

for _ in range(n + m):
    if (child := input()) not in kash:
        kash.add(child)
    else:
        kash.remove(child)

print(*(list(kash).sort()) if kash else "Таких нет", sep="\n")