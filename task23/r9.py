def f(n, fin):
    if n == fin:
        return 1
    if n > fin or n == 14:
        return 0
    return f(n + 1, fin) + f(n * 2, fin)


print(f(1, 10) * f(10, 20))