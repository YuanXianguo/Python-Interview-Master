"""
给定一个整数 n，返回 n! 结果尾数中零的数量。
"""


def trailingZeroes(n):
    cnt = 0
    while n >= 5:  # 考虑5 * 5的情况
        cnt += n // 5
        n //= 5
    return cnt


if __name__ == '__main__':
    print(trailingZeroes(30))
