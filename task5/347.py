def h(n):
    s1 = oct(n)[2:]
    for s in '1357':
        s1 = s1.replace(s, '2')
    s3 = s1 + str(n % 8)
    return int(s3, 8)


def f(n):
    return h(h(n))


s = 0
for n in range(10**4, 10**5):
    if f(n) % 2023 == 0:
        s += n
print(s)
