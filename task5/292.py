def f(n):
    step1 = f'{n:b}'
    sum_digit = sum(map(int, step1))
    if sum_digit % 2 == 0:
        # 2a
        step2 = '10' + step1[2:] + '0'
    else:
        # 2b
        step2 = '11' + step1[2:] + '1'
    return int(step2, 2)


for i in range(35):
    if f(i) < 35:
        print(i)