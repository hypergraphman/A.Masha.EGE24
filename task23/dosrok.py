def f(n, fin):
    if n == fin:
        return 1
    if n > fin or n == 20:
        return 0
    return f(n + 1, fin) + f(n + 2, fin) + f(n * 3, fin)


print(f(4, 10) * f(10, 22))