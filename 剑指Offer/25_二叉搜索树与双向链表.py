"""
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""
from sword_offer.binary_serach_tree import BinarySearchTree


def inorder(root, lst):
    inorder(root.left_child, lst)
    lst.append(root)
    inorder(root.right_child, lst)
    return lst


def tree_to_link_list(root):
    if not root:
        return
    lst = inorder(root, [])
    for i in range(len(lst)-1):
        lst[i].right_child = lst[i+1]
        lst[i+1].left_child = lst[i]
    return lst[0]


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(10):
        bst.insert(i)

    head = tree_to_link_list(bst.root)
    while head:
        print(head.elem, end=" ")
        head = head.right_child
