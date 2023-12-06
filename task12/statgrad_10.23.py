def is_prime(n):
    k = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            k += 2
            if k > 2:
                return False
    return True


a = []
for x in range(50):
    for y in range(50):
        p = 3 * x + 4 * y
        if x + y > 40 and is_prime(p):
            a.append(2 * x + y)
print(a)