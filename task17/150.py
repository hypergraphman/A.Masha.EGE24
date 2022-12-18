data = list(map(int, open('17-1.txt').readlines()))
# print(data)

k = 0
mn = 10**10
for i in range(1, len(data)):
    n1, n2 = data[i - 1], data[i]
    if n1 % 7 == 0 and n2 % 17 != 0 or n1 % 17 != 0 and n2 % 7 == 0:
        k += 1
        if n1 + n2 < mn:
            mn = n1 + n2
print(k, mn)