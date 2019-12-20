"""
题目：请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""
from sword_offer.binary_serach_tree import BinarySearchTree


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        def is_same(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val == root2.val:
                return is_same(root1.left, root2.right) and is_same(root1.right, root2.left)
            else:
                return False
        return is_same(pRoot, pRoot)


def is_sym_DFS(pRoot):
    """DFS"""
    if not pRoot:
        return True
    stack = [pRoot.left, pRoot.right]  # 成对插入
    while stack:
        right = stack.pop()  # 成对取出b
        left = stack.pop()
        if not right and not left:
            continue
        elif not right or not left:
            return False
        elif right.val != left.val:
            return False
        else:
            stack.append(left.right)
            stack.append(right.left)
            stack.append(left.left)
            stack.append(right.right)
    return True


def is_sym_BFS(pRoot):
    if not pRoot:
        return True
    from collections import deque
    q = deque()
    q.append(pRoot.left)
    q.append(pRoot.right)
    while q:
        right = q.popleft()
        left = q.popleft()
        if not left and not right:
            continue
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            q.append(left.right)
            q.append(right.left)
            q.append(left.left)
            q.append(right.right)
    return True


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add(0)
    bst.add(1)
    bst.add(1)
    bst.add(2)
    bst.add(3)
    bst.add(3)
    bst.add(2)
    bst.breadth_travel()
    s = Solution()
    print(s.isSymmetrical(bst.root))

    print(is_sym_DFS(bst.root))
    print(is_sym_BFS(bst.root))
