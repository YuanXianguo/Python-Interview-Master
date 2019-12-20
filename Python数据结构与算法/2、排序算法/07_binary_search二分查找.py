def binary_search(alist, item):
    """二分查找"""
    n = len(alist)
    if n:
        mid = n // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            binary_search(alist[:mid], item)
        else:
            binary_search(alist[mid+1:], item)
    return False


def binary_search2(alist, item):
    """二分查找，非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


def bin_search(array, target):
    """二分查找模板"""
    n = len(array)
    left, right = 0, n-1
    while left < right:
        mid = (left + right) >> 1
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    if array[left] == target:
        return left
    return -1


if __name__ == '__main__':
    arr = [i for i in range(10)]
    print(binary_search(arr, 11))
    print(binary_search2(arr, 11))
    print(bin_search(arr, 9))
    print(bin_search(arr, 11))
