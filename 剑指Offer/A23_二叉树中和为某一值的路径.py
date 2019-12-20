"""
题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""
from sword_offer.binary_serach_tree import BinarySearchTree, Node


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        self.res = []
        self.exp = expectNumber
        self.find_one(root, [], 0)
        return self.res

    def find_one(self, root, path, sum):
        sum += root.val
        path.append(root.val)
        if sum == self.exp and not root.left and not root.right:
            self.res.append(path[:])  # 由于共用path，所以需要添加path的副本到结果列表中
        elif sum < self.exp:
            if root.left:
                self.find_one(root.left, path, sum)
            if root.right:
                self.find_one(root.right, path, sum)
        path.pop()


class S(object):
    def main(self, root, num):
        if not root:
            return []
        self.res = list()
        self.get_path([], root, num)
        return self.res

    def get_path(self, path, root, num):
        path.append(root.val)
        num -= root.val
        if num == 0 and not root.left and not root.right:
            self.res.append(path[:])
        elif num > 0:
            if root.left:
                self.get_path(path, root.left, num)
            if root.right:
                self.get_path(path, root.right, num)
        path.pop()


class S2(object):
    def find(self, root, expectNumber):
        if not root:
            return []
        self.res = list()
        self.get_path([], root, expectNumber)
        return self.res

    def get_path(self, path, root, num):
        if not root:
            return
        num -= root.val
        path.append(root.val)
        if num == 0 and not root.left and not root.right:
            self.res.append(path[:])
        elif num > 0:
            if root.left:
                self.get_path(path, root.left, num)
            if root.right:
                self.get_path(path, root.right, num)
        path.pop()


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(10):
        bst.add(i)
    for i in range(50):
        s = Solution()
        print(i, s.FindPath(bst.root, i))
        s2 = S()
        print(i, s2.main(bst.root, i))
