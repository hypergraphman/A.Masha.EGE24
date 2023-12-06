def u1(x1, x2, x3):
    k = 0
    k += len(str(x1)) == 4
    k += len(str(x2)) == 4
    k += len(str(x3)) == 4
    return k == 2


def u2(x1, x2, x3):
    k = 0
    k += x1 % 3 == 0
    k += x2 % 3 == 0
    k += x3 % 3 == 0
    return k > 0


def u3(x1, x2, x3, e):
    return x1 + x2 + x3 > e


f = open('17.txt')
a = [int(x) for x in f]
e = max(filter(lambda x: x % 100 == 19, a))

z = []
for x1, x2, x3 in zip(a, a[1:], a[2:]):
    if u1(x1, x2, x3) and u2(x1, x2, x3) and u3(x1, x2, x3, e):
        z.append(x1 + x2 + x3)
print(len(z), max(z))