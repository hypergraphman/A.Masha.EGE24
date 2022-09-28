n = int(input())
sum_base = 0
sum_short = 0
sum_free = 0
for i in range(n):
    base = int(input())
    short = int(input())
    free = int(input())
    print(base, short, free)
    sum_base += base
    sum_short += short
    sum_free += free
print('Средний балл по обязательной программе: {:.2f}'.format(sum_base / n))
print('Средний балл по короткой программе: {:.2f}'.format(sum_short / n))
print('Средний балл по произвольной программе: {:.2f}'.format(sum_free / n))
