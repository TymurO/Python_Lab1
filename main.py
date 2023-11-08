def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def get_prime(num):
    index = 1
    res = 1
    while index < num:
        res += 2
        if is_prime(res):
            index += 1
    return res
