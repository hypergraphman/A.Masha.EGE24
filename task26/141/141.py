f = open('26-141.txt')
n = int(f.readline())
a = []
for line in f:
    a.append(tuple(map(int, line.split())))
a.sort(key=lambda pair: pair[1])

selfy = a[0][1]

k = 1
last = a[0]
for cur_lesson in a[1:]:
    if last[1] <= cur_lesson[0]:
        k += 1
        last = cur_lesson
print(k, selfy)