p = 55
mx_a = 0
val_mx_a = None
mn_a = p
val_mn_a = None
for x in range(0, p):
    n = (int('z', 36) * p**3 + x * p**2 + int('y', 36) * p + int('x', 36) -
         (2 * p**3 + int('x', 36) * p**2 + x * p + int('y', 36)))
    if n % 29 == 0:
        if x > mx_a:
            mx_a = x
            val_mx_a = n
        if x < mn_a:
            mn_a = x
            val_mn_a = n

print(abs(val_mn_a - val_mx_a))
print(mx_a, mn_a)
