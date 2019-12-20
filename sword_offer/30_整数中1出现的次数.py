"""题目：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数"""


def find_1(num):
    cnt = 0
    while num:
        if num % 10 == 1:
            cnt += 1
        num = num // 10

    return cnt


def get_all_1(start, end):
    cnt = 0
    for i in range(start, end+1):
        cnt += find_1(i)
    return cnt


if __name__ == '__main__':
    print(find_1(2121))
    print(get_all_1(1, 13))
    print(get_all_1(100, 1300))
