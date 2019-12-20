def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return alist

    mid_val = alist[first]  # 基准，中间值
    low, high = first, last
    while low < high:
        # high左移
        while low < high and mid_val <= alist[high]:
            high -= 1
        alist[low] = alist[high]
        # low右移
        while low < high and mid_val > alist[low]:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_val  # 此时low=high, 一次找到基准元素最终位置

    # 对low左边递归排序
    quick_sort(alist, first, low-1)
    # 对low右边递归排序
    quick_sort(alist, low+1, last)

    return alist


if __name__ == '__main__':
    li = [10-i for i in range(10)]
    print(li)
    print(quick_sort(li, 0, len(li)-1))
