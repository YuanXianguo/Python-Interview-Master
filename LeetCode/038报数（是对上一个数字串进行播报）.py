"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1
11
21
1211
111221
根据规律可以知道第六个数字串应念为 three 1 two 2 one 1得 6：312211

1 被读作 "one 1" ("一个一") , 即 11。

11 被读作 "two 1s" ("两个一"）, 即 21。

21 被读作 "one 2", "one 1" （"一个二" , "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
"""


def countAndSay(n):
    string = "1"  # n=0时string为1
    while n - 1:  # 对string进行递推n-1次
        tmp_s = string[0]  # 初始当前临时字符为上一次字符串首位
        cnt = 0  # 对当前字符计数
        tmp_str = ""   # 存储每次递推结果字符串
        for s in string:  # 对上次字符串进行遍历
            if s == tmp_s:  # 重复字符累加
                cnt += 1
            else:  # 遇到新字符将临时字符结合数量添加到结果字符串中
                tmp_str += str(cnt) + tmp_s
                tmp_s = s  # 更新临时字符
                cnt = 1  # 重置计数器
        tmp_str += str(cnt) + tmp_s  # 将最后一个字符添加到结果字符串中
        string = tmp_str  # 更新递推结果字符串
        n -= 1  # 更新n
    return string


class Solution:
    def countAndSay(self, n: int) -> str:
        if not n:
            return ""
        string = "1"
        while n > 1:
            this = ""
            tmp = string[0]
            cnt = 0
            for s in string:
                if s == tmp:
                    cnt += 1
                else:
                    this += str(cnt) + tmp
                    tmp = s
                    cnt = 1
            this += str(cnt) + tmp
            string = this
            n -= 1
        return string


if __name__ == '__main__':
    print(countAndSay(6))
    s = Solution()
    print(s.countAndSay(6))

