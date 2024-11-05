n = int(input())
d = {}
for _ in range(n):
    sur = input()
    d[sur] = d.get(sur, 0) + 1

print("\n".join(f"{sur} - {count}" 
      for sur, count in d.items() if count > 1)
      if d else "Однофамильцев нет")