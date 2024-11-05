n = int(input())
m = int(input())
kash = set()

for _ in range(n + m):
    if (child := input()) not in kash:
        kash.add(child)
    else:
        kash.remove(child)
kash_list = list(kash)
kash_list.sort()
print(*kash_list if kash else "Таких нет", sep=("\n" if kash else None))