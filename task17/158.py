data = list(map(int, open('17-1.txt').readlines()))

k = 1
mx_len = 1
cur_len = 1
for i in range(1, len(data)):
    el1, el2 = data[i - 1], data[i]
    if el1 > el2:
        cur_len += 1
        if cur_len > mx_len:
            k = 1
            mx_len = cur_len
        elif cur_len == mx_len:
            k += 1
    else:
        cur_len = 1
print(mx_len, k)

