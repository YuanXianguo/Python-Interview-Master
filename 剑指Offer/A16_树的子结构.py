"""
题目：输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""
from sword_offer.binary_serach_tree import BinarySearchTree


def treeB_in_treeA(rootA, rootB):
    """对树A进行遍历,如果树A某棵子树根等于树B的根进入子函数判断是否同构"""
    if not rootA or not rootB:
        return False
    res = False
    if rootA.elem == rootB.elem:  # 树A某棵子树根等于树B的根
        res = preorder(rootA, rootB)
    # 递归遍历子树A，直到返回True或False
    if not res:
        res = treeB_in_treeA(rootA.left_child, rootB)
    if not res:
        res = treeB_in_treeA(rootA.right_child, rootB)
    return res


def preorder(root1, root2):
    """判断子树1是否包含子树2"""
    if not root2:  # 子树2遍历完成
        return True
    if not root1:  # 子树2遍历未结束，子树1已经到叶结点
        return False
    elif root1.elem != root2.elem:  # 都不为空，但值不同
        return False
    # 都不为空，且相同，则递归进入下左右树
    res = preorder(root1.left_child, root2.left_child)
    res2 = preorder(root1.right_child, root2.right_child)
    return res and res2  # 只有左右子树同时返回True才为True


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        res = False
        if pRoot1.val == pRoot2.val:
            res = self.main(pRoot1, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def main(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.main(root1.left, root2.left) and self.main(root1.right, root2.right)


if __name__ == '__main__':
    treeA = BinarySearchTree()
    treeB = BinarySearchTree()
    for i in range(10):
        treeA.insert(i)
    for i in range(5):
        treeB.insert(i)
    print(treeB_in_treeA(treeA.root, treeB.root))
