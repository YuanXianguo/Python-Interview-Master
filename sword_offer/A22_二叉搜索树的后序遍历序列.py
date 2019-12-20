"""
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


def is_post_order(lst):
    if not lst:
        return False
    # 找到根结点
    root = lst[-1]
    index = 0

    # 左子树所有值需要满足小于根结点
    # 从左边开始遍历，找到第一个大于根结点的位置index，index及其右边为右子树
    for i in range(len(lst)-1):
        index = i
        if lst[i] > root:
            break
    # 右子树所有值需要满足大于根结点
    # 如果只有左子树，则如果从index开始遍历会返回False，
    # 所以从index+1开始，如果有右子树，因为index已经判断过，不会影响结果
    for i in range(index+1, len(lst)-1):
        if lst[i] < root:
            return False

    left = True
    if index:
        left = is_post_order(lst[0:index])

    right = True
    if index < len(lst) - 1:
        right = is_post_order(lst[index:len(lst)-1])

    return left and right


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        root = sequence[-1]
        index = 0
        for i in range(len(sequence) - 1):
            index = i
            if sequence[i] > root:
                break
        for i in range(index + 1, len(sequence) - 1):
            if sequence[i] < root:
                return False
        left = True
        right = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        if len(sequence)-1 > index:
            right = self.VerifySquenceOfBST(sequence[index:len(sequence)-1])
        return left and right


def is_post(arr):
    if not arr:
        return False

    # 左子树的值小于根结点，右子树的值大于根结点
    root = arr[-1]
    index = 0
    for i in range(len(arr)-1):
        index = i
        if arr[i] > root:
            break
    for i in range(index+1, len(arr)-1):
        if arr[i] < root:
            return False

    left, right = True, True
    if index > 0:
        left = is_post(arr[:index])
    if len(arr)-1 > index:
        right = is_post(arr[index:len(arr)-1])
    return left and right


def is_post2(sequence):
    if not sequence:
        return False
    index = 0
    n = len(sequence)
    root = sequence[-1]
    for i in range(n-1):
        index = i
        if sequence[i] > root:
            break
    for i in range(index+1, n-1):
        if sequence[i] < root:
            return False
    left = True
    if index > 0:
        left = is_post2(sequence[:index])
    right = True
    if n > index+1:
        right = is_post2(sequence[index:n])
    return left and right


if __name__ == '__main__':
    lst = [1, 3, 2, 6, 9, 8, 10, 5, 4]
    lst2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    lst3 = list(range(10))
    lst4 = [9, 7, 6, 5, 4, 3, 2, 1, 0, 8]
    lst5 = [2, 1, 3]

    print(is_post_order(lst))
    print(is_post_order(lst2))
    print(is_post_order(lst3))
    print(is_post_order(lst4))
    print(is_post_order(lst5))
    print("*"*100)

    s = Solution()
    print(s.VerifySquenceOfBST(lst))
    print(s.VerifySquenceOfBST(lst2))
    print(s.VerifySquenceOfBST(lst3))
    print(s.VerifySquenceOfBST(lst4))
    print(s.VerifySquenceOfBST(lst5))
