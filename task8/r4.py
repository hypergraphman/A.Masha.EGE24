from itertools import product

words = set()
alf = 'ЕГЭ'
for word_lets in product(alf, repeat=5):
    word = ''.join(word_lets)
    if word[0] in 'ЕЭ':
        words.add(word)
print(len(words))
