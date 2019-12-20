class Solution:
    def isValidBST(self, root):

        def is_valid_main(root, min, max):
            if not root:
                return True
            if min < root.val < max:
                # 左子树上限为根结点值，右子树下限为根结点值，遍历过程中不断更新上下限
                return is_valid_main(root.left, min, root.val) and is_valid_main(root.right, root.val, max)
            else:
                return False
        return is_valid_main(root, float("-inf"), float("inf"))  # 初始上下限为正负无穷


if __name__ == '__main__':
    from binary_serach_tree import BinarySearchTree
    bst = BinarySearchTree()
    for i in range(10):
        bst.insert(i)
    s = Solution()
    print(s.isValidBST(bst.root))

    bst2 = BinarySearchTree()
    for i in range(10):
        bst2.add(i)
    print(s.isValidBST(bst2.root))
