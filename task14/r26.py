p = 15
for x in range(0, p):
    n = (1 * p**4 + 2 * p**3 + 3 * p**2 + x * p + 5 +
         1 * p**4 + x * p**3 + 2 * p**2 + 3 * p + 3)
    if n % 14 == 0:
        print(n // 14)