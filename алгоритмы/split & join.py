line = input()
line_1 = line
s_w = 0
words = []
for i in range(len(line)):
    if line[i] == ' ':
        words.append(line[s_w:i])
        s_w = i + 1
words.append(line[s_w:])
# print(words)

words_1 = line_1.split()
print(words_1)

line_2 = '\n'.join(words_1)
print(line_2)
