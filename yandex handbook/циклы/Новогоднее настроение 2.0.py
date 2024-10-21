"""
Нужно вывести математическую елку вроде этой:
     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14
"""

n = int(input())
i = 1
nums_in_row = 1
all = []
while i < n + 1:
    row = []
    for num in range(nums_in_row):
        row.append(str(i))
        i += 1
        if i >= n + 1:
            break
    nums_in_row += 1
    all.append(row)
for row in all:
    print(f"{" ".join(row): ^{max(len(" ".join(all[-1])), len(" ".join(all[-2])) if len(all) > 1 else 0)}}")