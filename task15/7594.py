for a in range(1000):
    if all((x & 39 == 0) or ((x & 11 == 0) <= (not(x & a == 0))) for x in range(1000)):
        print(a)