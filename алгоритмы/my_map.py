def my_map(func, lst):
    new_list = []
    for el in lst:
        new_list.append(func(el))
    return new_list


def my_func(n):
    if n % 2 == 0:
        return (n + 2) % 10
    return n - 1


a = [1, 2, 8, 4]

b = my_map(my_func, a)

print(b)

c = ['123', '345', '348']
print(c)
n = 1234
print(sum(map(int, str(n))))
1234
'1234'
int('1')
int('2')