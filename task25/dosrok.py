from fnmatch import fnmatch

for i in range(211, 10**8, 211):
    if fnmatch(str(i), '12??1*56'):
        print(i, i // 211)