def isPowerOfTwo(n):
    if n < 1:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


if __name__ == '__main__':
    for i in range(50):
        print(i, isPowerOfTwo(i))
