for n in range(4, 100):
    line = '3' + '5' * n
    while '25' in line or '355' in line or '555' in line:
        if '25' in line:
            line = line.replace('25', '3')
        if '355' in line:
            line = line.replace('355', '52')
        if '555' in line:
            line = line.replace('555', '23')
    if sum(map(int, line)) == 27:
        print(n)
        break