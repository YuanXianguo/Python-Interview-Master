"""
题目：给定一颗二叉搜索树，请找出其中的第k大的结点。
例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
"""
from sword_offer.binary_serach_tree import BinarySearchTree


def KthNode(pRoot, k):
    # write code here
    stack = []
    while pRoot or stack:
        while pRoot:
            stack.append(pRoot)
            pRoot = pRoot.left
        if stack:
            pRoot = stack.pop()
            k -= 1
            if k == 0:
                return pRoot.val
            pRoot = pRoot.right


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k == 0:
            return None
        self.res = list()
        self.find(pRoot)
        return self.res[k-1] if k-1 < len(self.res) else None

    def find(self, pRoot):
        if not pRoot:
            return
        self.find(pRoot.left)
        self.res.append(pRoot)
        self.find(pRoot.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in [8,6,10,5,7,9,11]:
        bst.insert(i)
    print(KthNode(bst.root, 1))

    s = Solution()
    print(s.KthNode(bst.root, 1))
