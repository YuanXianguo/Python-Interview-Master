def max_child_lst(array):
    if not array or not len(array):
        return 0
    max_sum = array[0]
    cur_sum = 0
    for i in array:
        if cur_sum <= 0:
            cur_sum = i
        else:
            cur_sum += i
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


def max_child_lst2(array):
    if not array or not len(array):
        return 0
    if max(array) <= 0:
        return max(array)
    max_sum = 0
    cur_sum = 0
    for i in array:
        cur_sum += i
        if cur_sum <= 0:
            cur_sum = 0
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


def FindGreatestSumOfSubArray(array):
    # write code here
    dp = [array[0]] * len(array)
    for i in range(1, len(array)):
        dp[i] = max(array[i], dp[i-1] + array[i])
    return max(dp)


if __name__ == '__main__':
    print(max_child_lst([1, -2, 3, -4, 6, 8, -3]))
    print(max_child_lst2([-1,-2,-3,4]))

    print(FindGreatestSumOfSubArray([-1, -2, 3, -4, 6, 8, -3]))
