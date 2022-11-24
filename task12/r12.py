for i in range(247, 260):
    print(i)
    line = '2' * i
    while '222' in line or '555' in line:
        if '222' in line:
            line = line.replace('222', '5', 1)
        else:
            line = line.replace('555', '2', 1)
    print(line)

    line = '2' * i
    while '222' in line or '555' in line:
        if '555' in line:
            line = line.replace('555', '2', 1)
        else:
            line = line.replace('222', '5', 1)
    print(line)
