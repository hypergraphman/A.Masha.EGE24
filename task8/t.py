from itertools import product

words = [''.join(word) for word in product('САКУР', repeat=5)]
k = 0
for word in words:
    if word.count('А') <= 1 and word.count('У') <= 1:
        k += 1
print(k)