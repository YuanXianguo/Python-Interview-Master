def bubble_sort(array):
    n = len(array)
    for i in range(n-1, 0, -1):  # 每一趟需要比较的最后一个数索引
        flag = 1
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 0
        if flag:
            break
    return array


def select_sort(array):
    n = len(array)
    for i in range(n-1):  # 假定第i(从0开始)个数字最小（前面已经有序）
        min_num = i
        for j in range(i+1, n):
            if array[j] < array[min_num]:
                min_num = j
        array[i], array[min_num] = array[min_num], array[i]
    return array


def insert_sort(array):
    n = len(array)
    for i in range(1, n):  # 从第二个位置开始向前插入
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break
    return array


def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap:
        for i in range(gap, n):  # 内部与插入算法的区别就是gap步长
            for j in range(i, gap-1, -gap):
                if array[j-gap] > array[j]:
                    array[j-gap], array[j] = array[j], array[j-gap]
                else:
                    break
        gap //= 2
    return array


def quick_sort(array):
    def quick_sort_(array, start, end):
        if start >= end:
            return array

        flag = array[start]
        low = start
        high = end

        while low < high:
            while low < high and flag <= array[high]:
                high -= 1
            array[low] = array[high]
            while low < high and flag > array[low]:
                low += 1
            array[high] = array[low]

        array[low] = flag

        quick_sort_(array, start, low-1)
        quick_sort_(array, low+1, end)

        return array
    return quick_sort_(array, 0, len(array)-1)


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array

    mid = n // 2
    left_li = merge_sort(array[:mid])
    right_li = merge_sort(array[mid:])

    left, right = 0, 0
    res = list()
    while left < len(left_li) and right < len(right_li):
        if left_li[left] <= right_li[right]:
            res.append(left_li[left])
            left += 1
        else:
            res.append(right_li[right])
            right += 1

    res.extend(left_li[left:])
    res.extend(right_li[right:])

    return res


if __name__ == '__main__':
    import random
    arr = [i for i in range(-10, 10)]
    random.shuffle(arr)
    print(bubble_sort(arr))

    random.shuffle(arr)
    print(select_sort(arr))

    random.shuffle(arr)
    print(insert_sort(arr))

    random.shuffle(arr)
    print(shell_sort(arr))

    random.shuffle(arr)
    print(quick_sort(arr))

    random.shuffle(arr)
    print(merge_sort(arr))
