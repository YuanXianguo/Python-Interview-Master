def my_atoi(str):
    str = str.lstrip(" ")  # 去掉左端无效空白字符
    if not str:  # 如果字符串为空
        return 0

    def inner(str):
        """定义一个函数，以同时处理字符串首位为-和不为-的情况"""
        res = ""
        for s in str:
            if s.isdecimal():
                res += s
            else:
                break
        return int(res) if res else 0

    if str[0] == "-":
        res = -inner(str[1:])
        return max(res, -pow(2, 31))

    if str[0] == "+":
        str = str[1:]
    res = inner(str)
    return min(res, pow(2, 31)-1)


if __name__ == '__main__':
    print(my_atoi(""))
