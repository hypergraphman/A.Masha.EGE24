def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_check(password):
    nums = password.split(':')
    if len(nums) != 3:
        return False
    b, c = map(int, nums[1:])
    a = nums[0]
    return a == a[::-1] and is_prime(b) and c % 2 == 0


