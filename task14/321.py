from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    # dgts = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dgts = digits + ascii_uppercase
    while n > 0:
        d = n % p
        r = dgts[d] + r
        n //= p
    return r


print(n_to_p(3**72 + 6 * 3**50 - 7 * 3**26 + 2 * 3**15 + 155, 9).count('8'))
