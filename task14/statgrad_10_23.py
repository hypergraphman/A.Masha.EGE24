a = []
for x in range(37):
    for y in range(37):
        if (1 * 37 ** 7 + 2 * 37 ** 6 + x * 37 ** 5 + 6 * 37 ** 4 + 4 * 37 ** 3 + 3 * 37 ** 2 + y * 37 + 7) % 36 == 0:
           a.append(y * 37 + x)
print(max(a))
print(a)