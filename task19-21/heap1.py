# s > 125 win
# s > 160 lose
# s + 1
# s * 2
def f(s, c, m):
    if c > m:
        return False
    if s > 160:
        return c % 2 != m % 2
    if s >= 126:
        return c % 2 == m % 2
    moves = [f(s + 1, c + 1, m),
             f(s * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 126):
    for m in range(1, 5):
        if f(s, 0, m):
            print(s, m)
            break