"""
题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
from collections import deque
from sword_offer.binary_serach_tree import BinarySearchTree


def output_zhi(root):
    if not root:
        return
    q1 = deque()
    q2 = deque()
    q1.append(root)
    while q1 or q2:
        while q1:
            node = q1.popleft()
            print(node.elem, end=" ")
            if node.left_child:
                q2.append(node.left_child)
            if node.right_child:
                q2.append(node.right_child)
        print("")
        stack = []
        while q2:
            node = q2.popleft()
            stack.append(node.elem)
            if node.left_child:
                q1.append(node.left_child)
            if node.right_child:
                q1.append(node.right_child)
        while stack:
            print(stack.pop(), end=" ")
        print("")


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(10):
        bst.add(i)
    output_zhi(bst.root)
