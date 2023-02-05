a = {9, 10}
p = {2, 4, 9, 10, 15}
u = set(range(1, 22))
q = {3, 8, 9, 10, 20}

print(all([((x in p) == (x in a)) or ((x in q) == (x in a)) for x in range(1, 22)]))
