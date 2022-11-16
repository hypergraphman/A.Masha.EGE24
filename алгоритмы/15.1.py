n = int(input())
data = list(map(int, input().split()))
r = int(input())

t = data.pop(r)
i = len(data) - 1
while i != 0 and data[i] > t:
    i -= 1
data.insert(i + 1, t)

print(*data)