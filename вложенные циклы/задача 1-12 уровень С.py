for i in range(0, 11):
    for j in range(0, 11):
        if i == j == 0:
            print(end='   ')
        else:
            print('{:<3}'.format(i + j), end='')
    print()
