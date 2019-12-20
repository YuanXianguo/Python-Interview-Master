"""
题目：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
from collections import deque
from sword_offer.binary_serach_tree import BinarySearchTree


def output_level(root):
    """返回二维列表"""
    if not root:
        return []
    q1 = deque()
    q2 = deque()
    q1.append(root)
    lst = []
    while q1 or q2:
        lst1 = []
        while q1:
            node = q1.popleft()
            lst1.append(node.elem)
            if node.left_child:
                q2.append(node.left_child)
            if node.right_child:
                q2.append(node.right_child)
        lst.append(lst1)
        lst2 = []
        while q2:
            node = q2.popleft()
            lst2.append(node.elem)
            if node.left_child:
                q1.append(node.left_child)
            if node.right_child:
                q1.append(node.right_child)
        lst.append(lst2)
    return lst


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(10):
        bst.add(i)
    print(output_level(bst.root))
