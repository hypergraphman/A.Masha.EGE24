p = 158
s = 0
for x in range(0, p):
    n = (2 * p**4 + 7 * p**3 + 3 * p**2 + x * p + 2 +
         1 * p**4 + x * p**3 + 3 * p**2 + 9 * p)
    if n % 73 == 0:
        s += n // 73
        print(n // 73)
print(s)