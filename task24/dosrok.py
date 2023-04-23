from itertools import product

s = open('24dosrok.txt').read()
# print(s)
check_set = set(product('ABC', repeat=2))
cur_len = 1
max_len = 1
max_i = 0
for i, p in enumerate(zip(s, s[1:])):
    if (p[0], p[1]) not in check_set:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            max_i = i
    else:
        cur_len = 1

print(max_len)