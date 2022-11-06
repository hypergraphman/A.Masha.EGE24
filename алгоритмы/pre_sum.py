data = [37, 54, 78, 13, 37, 25]
pre_sum = [0]
for el in data:
    pre_sum.append(pre_sum[-1] + el)
start = 3
end = 5
print(pre_sum[5] - pre_sum[3 - 1])
