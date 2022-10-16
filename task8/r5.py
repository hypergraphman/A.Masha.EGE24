from itertools import product

words = set()
alf = 'ACGT'
for word_lets in product(alf, repeat=5):
    word = ''.join(word_lets)
    if word.count('A') == 2:
        words.add(word)
print(len(words))
