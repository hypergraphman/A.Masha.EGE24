a = [0] * 10
size = 0


def my_app(x):
    global size
    a[size] = x
    size += 1


def my_pop(i):
    global size
    t = a[i]
    for j in range(i, size - 1):
        a[j] = a[j + 1]
    size -= 1
    a[size] = 0
    return t


def my_ins(x, i):
    global size
    size += 1
    for j in range(size, i, -1):
        a[j] = a[j - 1]
    a[i] = x


my_app(3)
my_app(56)
my_app(-7)
my_app(6)
my_app(7)
my_app(70)

my_ins(0, 3)
print('----')
for i in range(size):
    print(a[i])