f = open('text.txt')
words = []
for line in f:
    words.extend(line.split())
new_words = []
for word in words:
    if 'ток' in word:
        new_words.append(word.lower().replace(',', '').replace('.', '').replace('!', ''))
# print(new_words)
k = 0
for word in new_words:
    if not (word[:3] == 'ток' or word[-3:] == 'ток'):
        print(word)
        k += 1
print(k)