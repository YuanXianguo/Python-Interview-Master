"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
"""


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0

        def find_sum(root, sum):
            if not root:
                return 0
            return int(root.val == sum) + find_sum(root.left, sum-root.val) + find_sum(root.right, sum-root.val)

        return find_sum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


class Solution2:
    cnt = 0

    def pathSum(self, root, sum: int) -> int:
        if not root:
            return 0
        self.path_main(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.cnt

    def path_main(self, root, sum):
        if not root:
            return
        sum -= root.val
        if sum == 0:
            self.cnt += 1
        if root.left:
            self.path_main(root.left, sum)
        if root.right:
            self.path_main(root.right, sum)


if __name__ == '__main__':
    from binary_serach_tree import BinarySearchTree
    bst = BinarySearchTree()
    ls = [10,5,-3,3,2,0,11,3,-2,0,1]
    for i in ls:
        bst.add(i)
    s = Solution()
    print(s.pathSum(bst.root, 8))
