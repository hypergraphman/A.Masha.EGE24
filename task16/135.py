from functools import cache


@cache
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1) - 1

for i in range(100, 1000, 100):
    f(i)
print(f(1000) / f(997))
