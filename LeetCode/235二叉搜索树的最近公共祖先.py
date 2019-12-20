"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
"""


def lowestCommonAncestor(root, p, q):
    """根据二叉搜索树的特性，最近公共祖先一定在p和q值之间"""
    if p.val > q.val:
        p, q = q, p
    while root:
        if root.val > q.val:
            root = root.left
        elif root.val < p.val:
            root = root.right
        else:
            return root
    return None
