"""то же самое, но повернуть"""

n = int(input())
m = int(input())
for row in range(n):
    for col in range(m):
        print(f"{(col * n + row + 1): >{len(str(m * n))}}", end=" ")
    print("")