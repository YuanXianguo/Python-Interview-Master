"""
题目：输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点
（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度
"""
from sword_offer.binary_serach_tree import BinarySearchTree


def get_height(root):
    if not root:
        return 0
    left = get_height(root.left_child)
    right = get_height(root.right_child)
    return 1 + max(left, right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(10):
        bst.insert(i)
    print(get_height(bst.root))
    print(get_height(bst.root.left_child))
    print(get_height(bst.root.right_child))


