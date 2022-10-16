from itertools import permutations

alf = 'КАПКАН'
words = set()
for word_lets in permutations(alf):
    word = ''.join(word_lets)
    if 'КК' not in word and 'АА' not in word:
        words.add(word)
print(len(words))