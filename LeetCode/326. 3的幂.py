def isPowerOfThree(n):
    if n < 1:
        return False
    while n > 1:
        if n % 3 == 0:
            n //= 3
        else:
            return False
    return True


if __name__ == '__main__':
    for i in range(-100, 100):
        print(i, isPowerOfThree(i))
