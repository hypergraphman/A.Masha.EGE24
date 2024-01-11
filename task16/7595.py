from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    return n + 3 + f(n + 3)


for i in range(2025, 0, -1):
    f(i)

print(f(23) - f(21))