from itertools import product

words = set()
for word in map(''.join, product('0123456789ab', repeat=7)):
    if word[0] != '0' and word.count('b') == 2:
        words.add(word)
print(len(words))

res = []
for word in words:
    word = word.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0').replace('a', '0')
    word = word.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1').replace('b', '1')
    if '00' not in word and '11' not in word:
        res.append(word)
print(len(res))
# print(len(words) - len(res))