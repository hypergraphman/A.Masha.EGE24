n = int(input())
names = ('обязательной', 'короткой', 'произвольной')
sum_points = [0, 0, 0]
for i in range(n):
    points = []
    for j in range(3):
        points[j].append(int(input()))
        sum_points[j] += points[j]
    for j in range(len(points)):
        print(points[j], end=' ')
    print()
for i, name in enumerate(names):
    print('Средний балл по {} программе: {:.2f}'.format(name, sum_points[i] / n))
