f = open('17_7596.txt')
a = [int(x) for x in f]
mn = float('inf')
for el in a:
    if 100 <= abs(el) <= 999 and abs(el) % 10 == 5:
        mn = min(mn, el)

b = []
for p1, p2 in zip(a, a[1:]):
    if (100 <= abs(p1) <= 999) + (100 <= abs(p2) <= 999) == 1 and (p1 + p2) % mn == 0:
        b.append(p1 + p2)
print(len(b), min(b))