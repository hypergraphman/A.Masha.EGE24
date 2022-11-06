data = open('9-170.txt').readlines()
c = 0
for line in data:
    nums = list(map(int, line.split()))
    set_nums = set(nums)
    if len(nums) - 1 == len(set_nums):
        t = sum(nums) - sum(set_nums)
        if (sum(set_nums) - t) / 4 <= t + t:
            c += 1
print(c)
