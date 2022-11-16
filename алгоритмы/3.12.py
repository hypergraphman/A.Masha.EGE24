n = input()
a = []
for el in n:
    if el not in a:
        a.append(el)
a.insert(0, a.pop())
print(*a, sep='')
