"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""
cnt = 0
for i in range(1,100):
    if (2 * i - 1) % 7 == 0:
        cnt += 1
print(cnt)

def reverseWords(s):
    lst = s.split(" ")
    for i, v in enumerate(lst):
        lst[i] = v[::-1]
    return " ".join(lst)


if __name__ == '__main__':
    print(reverseWords(""))
    print(reverseWords("Let's take LeetCode contest"))
