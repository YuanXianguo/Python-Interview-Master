"""
题目：输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
import heapq


def get_min_nsmall(array, k):
    """调用nsmallest方法"""
    if not array or len(array) < k or k <= 0:
        return []
    return heapq.nsmallest(k, array)


def get_min_sort(array, k):
    """堆排序"""
    heapq.heapify(array)
    return [heapq.heappop(array) for i in range(k)]


if __name__ == '__main__':
    print(get_min_nsmall([4,5,1,6,2,7,3,8], 4))
    print(get_min_sort([4,5,1,6,2,7,3,8], 4))
