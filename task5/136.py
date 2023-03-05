def f(n):
    s1 = bin(n)[2:]
    # if s1.count('1') % 2 == 0:
    #     s2 = s1 + '0'
    # else:
    #     s2 = s1 + '1'
    s2 = s1 + str(s1.count('1') % 2)
    s3 = s2 + str(s2.count('1') % 2)
    return int(s3, 2)


s = set()
for i in range(1, 16):
    s.add(f(i))
r = set(range(16, 32 + 1))
print(len(r - s))