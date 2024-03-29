"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

"""

class Solution:
    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


if __name__ == '__main__':
    s = Solution()
    from tree import Tree
    t1 = Tree()
    t2 = Tree()
    for i in range(5):
        t1.add(i)
        # t2.add(i)
    root = s.mergeTrees(t1.root, t2.root)
    t = Tree(root)
    t.breadth_travel()
