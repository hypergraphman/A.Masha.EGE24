from re import fullmatch
from functools import reduce

data = list(map(int, open('17-346.txt').readlines()))
k = 0
mx = 0
limit = 2 * 10**9
for i in range(2, len(data)):
    el1, el2, el3 = data[i - 2], data[i - 1], data[i]
    t = list(map(int, str(el1))) + list(map(int, str(el2))) + list(map(int, str(el3)))
    p = reduce(lambda x, y: x * y, t)
    if p <= limit and fullmatch(r'43\d*6\d*', str(p)):
        k += 1
        mx = max(p, mx)
print(k, mx)
