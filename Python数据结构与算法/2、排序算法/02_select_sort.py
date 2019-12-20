def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for i in range(n-1):  # 假定第i(从0开始)个数字最小（前面已经有序）
        min_index = i
        for j in range(i+1, n):  # 从i+1开始依次比较
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


if __name__ == '__main__':
    print(select_sort([2,3,5,1,4]))
