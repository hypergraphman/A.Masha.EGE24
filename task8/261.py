from itertools import product

alf = 'АЕЖЙМУ'
aa = [let * 2 for let in alf]
words = set()
for i, word_letters in enumerate(product(alf, repeat=5), start=1):
    word = ''.join(word_letters)
    if (all([let not in word for let in aa]) and
       i % 2 == 0):
        words.add(word)
print(len(words))