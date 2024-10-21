"""
числовая змейка вроде этой:
 1  2  3  4  5  6
12 11 10  9  8  7
13 14 15 16 17 18
24 23 22 21 20 19
"""

n = int(input())
m = int(input())
for row in range(n):
    for col in range(m):
        print(f"{(col + row * m + 1 if row % 2 != 1 else (row + 1) * m - col): >{len(str(m * n))}}", end=" ")
    print("")