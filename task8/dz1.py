from itertools import permutations

words = set()
for word in map(''.join, permutations('anastasiy')):
    words.add(word)
# print(len(words))

res = []
for word in words:
    word = word.replace('i', 'a').replace('y', 'a').replace('n', 's').replace('t', 's')
    if 'aaa' not in word or 'sss' not in word:
        res.append(word)
print(len(res))
# print(len(words) - len(res))