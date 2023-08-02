def n_to_3(n):
    r = ''
    while n > 0:
        r = '012'[n % 3] + r
        n //= 3
    return r


def f(n):
    r = n_to_3(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + n_to_3(n % 3 * 4)
    return int(r, 3)


m = 0
for n in range(2, 100):
    if f(n) < 199:
        m = max(m, n)
print(m)