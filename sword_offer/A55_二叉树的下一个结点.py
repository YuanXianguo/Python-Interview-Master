"""
题目：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class Node(object):
    def __init__(self, elem=None):
        self.elem = elem
        self.left = None
        self.right = None
        self.parent = None


def get_next(node):
    if not node:
        return
    next = None

    # 如果有右结点，则下一个结点为右子树最左结点
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        next = node

    # 如果当前结点有父结点且当前结点为父结点左结点，则下一个结点为父结点
    if node.parent and node.parent.left == node:
        next = node.parent

    # 如果当前结点有父结点且当前结点为父结点右结点，则往上遍历
    # 当遍历到当前结点为父结点的左结点时，则下一个结点为当前节点的父结点
    if node.parent and node.parent.right == node:
        node = node.parent
        while node.parent and node.parent.right == node:
            node = node.parent
        # 遍历结束时当前结点有父结点，说明当前结点时父结点的左结点，
        # 则下一个结点为当前结点的父结点
        # 反之，说明当前结点位于根结点的右子树的最右结点，没有下一个结点
        if node.parent:
            next = node.parent

    return next


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        """
        分析二叉树的下一个结点，主要有以下几种情况：
        1.二叉树为空，返回空
        2.结点右孩子存在，则下一个结点为右孩子的最左结点
        3.结点右孩子不存在，但结点有父结点：
        （1）该结点是父结点的左孩子，则返回父结点
        （2）该结点是父结点的右孩子，则继续向上遍历其父结点的父结点，直到找到某个父结点A为其父结点B的左孩子，返回A的父结点B
        4.结点为右子树的最右结点，无下一个结点
        """
        if not pNode:
            return
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next


def next(pNode):
    # 右子树存在
    if pNode.right:
        node = pNode.right
        while node.left:
            node = node.left
        return node

    # 父结点存在
    while pNode.next:
        if pNode.next.left == pNode:
            return pNode.next
        pNode = pNode.next


def next2(pNode):
    if pNode.right:
        node = pNode.right
        while node.left:
            node = node.left
        return node
    while pNode.next:
        if pNode.next.left == pNode:
            return pNode.next
        pNode = pNode.next
