from itertools import permutations


def check(word):
    c = 0
    for let1, let2 in zip(word, 'тихо'):
        if let1 == let2:
            c += 1
    return c == 2


alf = 'тихорецк'
gl = set('иое')
words = set()
for word in permutations(alf, r=4):
    word = ''.join(word)
    if len(set(word) & gl) == 2 and check(word):
        words.add(word)
print(len(words))