n = int(input())
width = len(str(int((n + 1) / 2)))
for row in range(n):
    for col in range(n):
        if row < n / 2 and col < n / 2:
            print(f'{min(row, col) + 1: >{width}}', end=" ")
        elif row < n / 2 and col >= n / 2:
            print(f'{min(n - col, row + 1): >{width}}', end=" ")
        elif row >= n / 2 and col < n / 2:
            print(f'{min(n - row, col + 1): >{width}}', end=" ")
        else:
            print(f'{n - max(row, col): >{width}}', end=" ")
    print("")