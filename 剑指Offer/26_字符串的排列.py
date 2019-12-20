"""
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


def get_sequence(str):
    if not str:
        return
    if len(str) == 1:
        return str
    lst = []
    for s in str:  # 将字符串依次取出来一个字符，剩余的递归
        index = str.index(s)
        tmp = get_sequence(str[:index]+str[index+1:])
        for ss in tmp:
            lst.append(s+ss)  # 将取出来的字符和递归结果依次拼接并添加到一个列表
    return lst


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        self.res = list()
        self.main(ss, "")
        # return self.res
        return sorted(list(set(self.res)))

    def main(self, ss, path):
        if ss == "":
            self.res.append(path)
            return
        else:
            for i in range(len(ss)):
                self.main(ss[:i] + ss[i + 1:], path + ss[i])


if __name__ == '__main__':
    str = "abca"

    print(get_sequence(str))

    s = Solution()
    print(s.Permutation(str))

