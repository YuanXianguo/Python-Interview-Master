"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
"""


class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        res = []
        self.get_length(root, res)
        return max(res) - 1

    def get_length(self, root, res):
        if not root:
            return 0
        left = self.get_length(root.left, res)
        right = self.get_length(root.right, res)
        res.append(left + right + 1)
        return max(left, right) + 1


class Solution2:
    def diameterOfBinaryTree(self, root) -> int:
        self.dis = 0
        self.main(root)
        return self.dis

    def main(self, root):
        if not root:
            return 0
        left = self.main(root.left)
        right = self.main(root.right)
        self.dis = max(self.dis, left + right)
        return max(left, right) + 1


if __name__ == '__main__':
    s = Solution()
    from binary_serach_tree import BinarySearchTree
    bst = BinarySearchTree()
    for i in range(1, 6):
        bst.insert(i)
    bst.inorder()
    bst.breadth_travel()
    print(s.diameterOfBinaryTree(bst.root))
