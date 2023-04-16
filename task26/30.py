n, *a = map(int, open('26-j5.txt'))
b = [a[0]]
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    b.append(sorted([p1, p2, p3])[1])
b.append(a[-1])
ans_2 = 0
for p1, p2 in zip(a, b):
    if p1 > p2:
        ans_2 += p1 - p2
print(b.count(min(b)), ans_2)