def n_to_p(n, p=2):
    s = ''
    alp = '0123456789ABCDEF'
    while n > 0:
        s = alp[n % p] + s
        n = n // p
    return s


print(n_to_p(147))
print(int('1234', 5))
print(bin(100)[2:])
print(f'{100:x}')
