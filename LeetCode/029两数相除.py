"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。
"""


def divide(dividend, divisor):
    if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
        sign = 1  # 判断是否异号
    else:
        sign = -1
    m = 1  # 记录当前除数是原除数的倍数
    cnt = 0  # 记数
    dd, dr = abs(dividend), abs(divisor)
    while dd >= abs(divisor):
        if dd < dr:  # 如果当前除数太大，就重置除数
            dr = abs(divisor)
            m = 1
        dd -= dr
        cnt += m
        dr <<= 1  # 除数扩大为2倍
        m <<= 1  # 更新倍数
    if sign == - 1:  # 如果异号
        cnt = -cnt
    if cnt < -pow(2, 31) or cnt > pow(2, 31) - 1:
        cnt = pow(2, 31) - 1
    return cnt


class Solution:
    def divide(self, dividend: int, divisor: int):
        n = 1
        cnt = 0
        tmp_ds = abs(divisor)
        tmp_dd = abs(dividend)
        while tmp_dd >= abs(divisor):
            tmp_dd -= tmp_ds
            cnt += n

            tmp_ds += tmp_ds  # 更新除数和倍数
            n += n

            if tmp_dd < tmp_ds:  # 重置除数和倍数
                tmp_ds = abs(divisor)
                n = 1

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        if sign < 0:
            cnt = - cnt
        if not - pow(2, 31) <= cnt <= pow(2, 31) - 1:
            cnt = pow(2, 31) - 1
        return cnt


if __name__ == '__main__':
    print(divide(10, 3))
    print(divide(10, 2))
    print(divide(-1, -1))
    print(divide(-1, 1))
    print(divide(10, -2))
    print(divide(10, -3))

