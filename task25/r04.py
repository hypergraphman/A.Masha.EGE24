for i in range(2023, 10**10, 2023):
    t = str(i)
    if t[0] == '1' and t[2:6] == '2139' and t[-1] == '4':
        print(i, i // 2023)


from re import fullmatch
for i in range(2023, 10**10, 2023):
    if fullmatch(r'1\d2139\d*4', str(i)):
        print(i, i // 2023)