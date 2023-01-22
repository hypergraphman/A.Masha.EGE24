d = dict()
for line in open('22-28.txt').readlines():
    n, t, a = line.split('\t')
    t = int(t)
    a = a.strip().strip('"').split('; ')
    d[n] = [t, a]
print(d)
for i in d:
    if d[i][1][0] != '0':
        # mx = -1
        # for el in d[i][1]:
        #     if d[el][0] > mx:
        #         mx = d[el][0]
        # d[i][0] += mx
        d[i][0] += d[max(d[i][1], key=lambda x: d[x][0])][0]
print(max(d.values(), key=lambda x: x[0])[0])