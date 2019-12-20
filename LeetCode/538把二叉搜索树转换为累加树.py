"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和
"""


class Solution:

    def convertBST(self, root):
        self.res = []
        self.travel(root)
        if not self.res:
            return
        for i in range(len(self.res)-2, -1, -1):
            self.res[i].val += self.res[i+1].val
        return root

    def travel(self, root):
        if not root:
            return
        self.travel(root.left)
        self.res.append(root)
        self.travel(root.right)


class Solution2:

    def convertBST(self, root):
        self.sum = 0
        self.travel(root)
        return root

    def travel(self, root):
        if not root:
            return
        self.travel(root.right)
        self.sum += root.val
        root.val = self.sum
        self.travel(root.left)


if __name__ == '__main__':
    from binary_serach_tree import BinarySearchTree
    t = BinarySearchTree()
    for i in range(5):
        t.insert(i)
    t.inorder()
    s = Solution()
    new_r = s.convertBST(t.root)
    t.inorder()
    new_t = BinarySearchTree(new_r)
    new_t.inorder()

    t = BinarySearchTree()
    for i in range(5):
        t.insert(i)
    t.inorder()
    s = Solution2()
    new_r = s.convertBST(t.root)
    t.inorder()
    new_t = BinarySearchTree(new_r)
    new_t.inorder()

