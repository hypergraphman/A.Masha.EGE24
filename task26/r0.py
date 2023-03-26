for i in range(1, 21):
    v, n, *a = map(int, open(f'26-{i}.txt').read().split())
    a.sort()
    k = 0
    while k < len(a) and v - a[k] >= 0:
        v -= a[k]
        k += 1
    print(k, end=' ')
    v += a[k - 1]
    while k < len(a) and v - a[k] >= 0:
        k += 1
    print(a[k - 1])
