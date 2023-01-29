s = open('24.txt').read()
# print(s)
cur_len = 1
max_len = 1
max_i = 0
for i, p in enumerate(zip(s, s[1:])):
    if p[0] != p[1]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            max_i = i
    else:
        cur_len = 1

print(max_len, s[max_i - max_len + 2: max_i + 2])