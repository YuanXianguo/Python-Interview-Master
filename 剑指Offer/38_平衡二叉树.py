"""
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""
def is_balance(pRoot):
    if not pRoot:
        return True

    def get_length(root):
        if not root:
            return 0
        len_left = get_length(root.left)
        len_right = get_length(root.right)
        if len_left < 0 or len_right < 0 or abs(len_left - len_right) > 1:
            return -1
        return 1 + max(len_left, len_right)

    return get_length(pRoot) > -1


if __name__ == '__main__':
    from sword_offer.binary_serach_tree import BinarySearchTree
    bst = BinarySearchTree()
    for i in range(10):
        bst.insert(i)
    for i in range(-10, -1):
        bst.insert(i)

    print(is_balance(bst.root))
