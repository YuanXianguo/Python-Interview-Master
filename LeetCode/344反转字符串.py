"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
"""


def reverseString(s):
    if len(s) >= 2:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    reverseString(s)
    print(s)

    s = ["H","a","n","n","a","h"]
    reverseString(s)
    print(s)
