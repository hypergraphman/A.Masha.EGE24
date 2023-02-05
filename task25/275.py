for y in range(1, 10):
    t = '3254' + str(y) + '123'
    if int(t) % 519 == 0 and sum(map(int, t[:len(t) // 2])) == sum(map(int, t[len(t) // 2:])):
        print(t, int(t) // 519)

for x in range(1, 10**5):
    for y in range(1, 10):
        t = '32' + str(x) + '54' + str(y) + '123'
        if len(t) % 2 == 0 and '0' not in t and int(t) % 519 == 0 and sum(map(int, t[:len(t) // 2])) == sum(map(int, t[len(t) // 2:])):
            print(t, int(t) // 519)