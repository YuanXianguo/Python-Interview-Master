"""完全数，等于所有因子的和的数；例如：28 = 1 + 2 + 4 + 7 + 14"""


def is_complete(num):
    if num == 1:
        return True
    if num == 2:
        return False
    sum_ = 1  # 循环不判断1，直接把1计入总和
    left, right = 2, num-1
    while left <= right:
        if left * right < num:
            left += 1
        elif left * right > num:
            right -= 1
        else:
            sum_ += (left + right)
            left += 1
            right += 1
    if sum_ == num:
        return True
    return False


for i in range(1, 1000):
    if is_complete(i):
        print(i)

