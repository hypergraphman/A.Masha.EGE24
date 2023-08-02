a = [1, 4, 2, 9, 6, 3, 2, -9, 4, 7]
i_mx = 0
for i in range(1, len(a)):
    if a[i] > a[i_mx]:
        i_mx = i
print(a[i_mx], i_mx)