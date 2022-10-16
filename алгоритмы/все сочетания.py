from itertools import product

alf = 'aabc'
for el in product(alf, repeat=4):
    print(el)