"""
题目：操作给定的二叉树，将其变换为源二叉树的镜像。
"""
from sword_offer.binary_serach_tree import BinarySearchTree


def get_mir(root):
    if not root:
        return
    tmp = get_mir(root.right_child)
    root.right_child = get_mir(root.left_child)
    root.left_child = tmp
    return root


if __name__ == '__main__':
    tree = BinarySearchTree()
    for i in range(10):
        tree.insert(i)
    tree.inorder()
    print("")
    root = get_mir(tree.root)
    new_tree = BinarySearchTree(root)
    new_tree.inorder()
