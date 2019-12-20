"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

def is_palindrome(x):
    if x < 0:
        return False
    if x == int(str(x)[::-1]):
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome(-121))
    print(is_palindrome(121))
    print(is_palindrome(21))
    print(is_palindrome(+121))



