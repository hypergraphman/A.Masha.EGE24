n = int(input())
res = {'обязательной': 0, 'короткой': 0, 'произвольной': 0}
all_points = []
for i in range(n):
    points = []
    for name in res.keys():
        points.append(int(input()))
        res[name] += points[-1]
    all_points.append(points)
    for j in range(len(points)):
        print(points[j], end=' ')
    print()
for i, name in enumerate(res.keys()):
    print('Средний балл по {} программе: {:.2f}'.format(name, res[name] / n))

for i in range(len(all_points)):
    for j in range(len(all_points[i])):
        print(all_points[i][j], end=' ')
    print()
