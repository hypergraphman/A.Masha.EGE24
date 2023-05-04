for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (z or not(x <= y)) <= ( w and x)
                print(x, y, z, w, int(f))