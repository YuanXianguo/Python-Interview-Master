class Solution:
    # 返回对应char
    def __init__(self):
        self.string = ""
        self.dic = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.string:
            if self.dic[i] == 1:
                return i
        return "#"

    def Insert(self, char):
        # write code here
        self.string += char
        self.dic[char] = self.dic.get(char, 0) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.FirstAppearingOnce())
