def count_num(lst, num):
    return lst.count(num)


def count_bin(lst, num):
    """二分查找"""
    if not lst or not len(lst):
        return 0
    first = get_first_index(lst, num, 0, len(lst))
    last = get_last_index(lst, num, 0, len(lst))
    return last - first + 1


def get_first_index(lst, num, start, end):
    """找到第一次出现的索引"""
    if start > end:
        return -1
    middle = (start + end) // 2
    if lst[middle] > num:
        end = middle - 1
    elif lst[middle] < num:
        start = middle + 1
    else:  # 找到一个num，如果前一个也是num，就向前半段查找
        if middle > 0 and lst[middle - 1] == num:
            end = middle - 1
        else:  # 当前num是第一个，返回
            return middle

    return get_first_index(lst, num, start, end)


def get_last_index(lst, num, start, end):
    """找到最后一次出现的索引"""
    if start > end:
        return -1
    middle = (start + end) // 2
    if lst[middle] > num:
        end = middle - 1
    elif lst[middle] < num:
        start = middle + 1
    else:
        if middle > 0 and lst[middle + 1] == num:
            start = middle + 1
        else:
            return middle

    return get_last_index(lst, num, start, end)


if __name__ == '__main__':
    print(count_num([1, 2, 2, 2, 3], 2))
    print(count_bin([1, 2, 2, 2, 3], 2))
