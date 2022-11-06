from itertools import permutations

words = set()
for letters_word in permutations('ВУАЛЬ'):
    word = ''.join(letters_word)
    if word[0] != 'Ь' and 'ЬА' not in word and 'ЬУ' not in word:
        words.add(word)
print(len(words))
