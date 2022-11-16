n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = []
for i in range(n):
    a.append([x[i], y[i]])
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([x[i], y[i]])
min_value = 10**10
min_point_a = None
min_point_b = None
for point_a in a:
    for point_b in b:
        x1, y1 = point_a[0], point_a[1]
        x2, y2 = point_b[0], point_b[1]
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if min_value > distance:
            min_value = distance
            min_point_a = point_a
            min_point_b = point_b
print(*min_point_a)
print(*min_point_b)
