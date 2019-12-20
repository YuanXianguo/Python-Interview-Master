def intToRoman(num):
    # 定义一个映射表rom,其每个元素列表对应一组1，5，10（10，50，100；100，500，1000）
    rom = [["I", "V", "X"], ["X", "L", "C"], ["C", "D", "M"]]
    # 将输入数字补位成为一个4为字符串，不足补0，以统一处理
    str_num = "{:0>4}".format(num)
    res = "M" * int(str_num[0])
    for i in range(1, 4):
        if int(str_num[i]) == 9:  # IX
            res += rom[-i][0] + rom[-i][2]
        elif 5 <= int(str_num[i]) < 9:  # V(I * n),n=0,1,2,3
            res += rom[-i][1] + rom[-i][0] * (int(str_num[i]) - 5)
        elif int(str_num[i]) == 4:  # IV
            res += rom[-i][0] + rom[-i][1]
        else:  # I * n,n=0,1,2,3
            res += rom[-i][0] * (int(str_num[i]))
    return res


class Solution:
    def intToRoman(self, num: int) -> str:
        map = [["M"], ["C", "D", "M"],  ["X", "L", "C"], ["I", "V", "X"]]
        num_str = "{:0>4}".format(num)
        res = ""
        for i in range(4):
            if int(num_str[i]) < 4:
                res += map[i][0] * int(num_str[i])
            elif int(num_str[i]) == 4:
                res += map[i][0] + map[i][1]
            elif int(num_str[i]) < 9:
                res += map[i][1] + map[i][0] * (int(num_str[i]) % 5)
            elif int(num_str[i]) == 9:
                res += map[i][0] + map[i][2]
        return res


if __name__ == '__main__':
    print(intToRoman(3))
    print(intToRoman(4))
    print(intToRoman(9))
    print(intToRoman(58))
    print(intToRoman(1994))



