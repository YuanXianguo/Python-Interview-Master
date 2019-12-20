"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
"""


def merge(nums1, m, nums2, n):
    while m and n:
        if nums1[m-1] > nums2[n-1]:
            # m+n-1表示未排序末尾索引等于需要排序的总数量-1，赋值为未排序部分较大值
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    while n:  # 数组2排序完毕，1未完毕，则排序结束；反之，需要将数组2剩余未排序部分赋值到数组1
        nums1[n-1] = nums2[n-1]
        n -= 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        tmp = list()
        index1, index2 = 0, 0
        while index1 < m and index2 < n:
            if nums1[index1] <= nums2[index2]:
                tmp.append(nums1[index1])
                index1 += 1
            else:
                tmp.append(nums2[index2])
                index2 += 1
        while index1 < m:
            tmp.append(nums1[index1])
            index1 += 1
        index = index1 + index2
        for i in range(index):
            nums1[i] = tmp[i]
        for i in range(n - index2):
            nums1[index + i] = nums2[index2 + i]

            
if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    merge(nums1, m, nums2, n)

    print(nums1)
