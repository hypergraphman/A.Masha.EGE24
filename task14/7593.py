for x in range(0, 16):
    op1 = 9 * 15**7 + 7 * 15** 6 + 9 * 15**5 + 6*15**4 + 8 * 15**3 + x * 15**2 + 1 * 15 + 3
    op2 = 7 * 15**4 + x * 15**3 + 2 * 15**2 + 15 + 3
    if (op1 + op2) % 14 == 0:
        print((op1 + op2) // 14)