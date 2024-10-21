"""
числовая змейка вроде этой:
 1  8  9 16 17 24
 2  7 10 15 18 23
 3  6 11 14 19 22
 4  5 12 13 20 21
"""

n = int(input())
m = int(input())
for row in range(n):
    for col in range(m):
        print(f"{(col * n + row + 1 if col % 2 != 1 else (col + 1) * n - row): >{len(str(m * n))}}", end=" ")
    print("")