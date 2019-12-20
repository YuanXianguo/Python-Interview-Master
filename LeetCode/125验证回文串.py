"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
"""


def isPalindrome(s):
    if not s:
        return True
    left, right = 0, len(s)-1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
