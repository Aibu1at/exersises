nums = [int(x) for x in input().split()]
gcd = min(nums)
for num in nums:
    while num:
        num, gcd = gcd % num, num
print(gcd)