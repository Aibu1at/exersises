n = int(input())
d = {}
for _ in range(n):
    name, *porriges = input().split()
    for porrige in porriges:
        d[porrige] = d.get(porrige, []) + [name]

req = input()

print("\n".join(sorted(d[req])) if req in d else "Таких нет")