def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for i in range(1, n):  # 从第二个位置开始向前插入
        # 从右边无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的有序序列中
        for j in (i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break


if __name__ == '__main__':
    print(insert_sort([3,6,1,2,8,4,9,7]))
