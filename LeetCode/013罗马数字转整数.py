"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""


def romanToInt(s):
    # 定义一个映射字典
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    flag = 0
    while flag < len(s) - 1:  # 对字符串进行遍历
        # 如果某位字符串的下一位字符在自定义字典中对应的值比它小，即为特例之外的情况
        # 在通常情况下，将当前位转换为映射值，并右移一位
        if rom[s[flag + 1]] <= rom[s[flag]]:
            res += rom[s[flag]]
            flag += 1
        else:  # 如果某位字符串的下一位字符在自定义字典中对应的值比它大，即为特例
            # 在特例情况下，通过组合字符将当前位和下一位一起转换为罗马值，并右移两位
            res += (rom[s[flag + 1]] - rom[s[flag]])
            flag += 2
    # 循环结束后，当前索引可能大于最后一位，则遍历结束；当前索引等于最后一位，则对最后一位转换
    if flag == len(s) - 1:
        res += rom[s[-1]]
    return res


if __name__ == '__main__':
    print(romanToInt("I"))
    print(romanToInt("II"))
    print(romanToInt("III"))
    print(romanToInt("IV"))
    print(romanToInt("IX"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))




