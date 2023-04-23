p = 15
for x in range(0, p):
    n = (9 * p ** 7 + 7 * p ** 6 + 9 * p ** 5 + 6 * p ** 4 + 8 * p ** 3 + x * p ** 2 + 2 * p + 1 +
         7 * p ** 3 + x * p ** 2 + 2 * p + 3)
    if n % 14 == 0:
        print(n // 14)
