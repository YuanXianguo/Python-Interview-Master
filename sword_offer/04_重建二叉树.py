"""
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""
from sword_offer.tree import Tree


class Node(object):
    def __init__(self, elem=None):
        self.elem = elem
        self.left_child = None
        self.right_child = None


def get_tree(pre_lst, in_lst):
    """接收前序和中序遍历结果的列表，返回一棵树的根结点"""
    if not pre_lst:
        return
    else:
        root = Node(pre_lst[0])
        root_index = in_lst.index(pre_lst[0])
        root.left_child = get_tree(pre_lst[1:root_index+1], in_lst[:root_index])
        root.right_child = get_tree(pre_lst[root_index+1:], in_lst[root_index+1:])
        # 接收后序和中序遍历结果的列表，返回一棵树的根结点：
        # root = Node(post_lst[-1])
        # root_index = in_lst.index(post_lst[-1])
        # get_tree(post_lst[:root_index], in_lst[:root_index])
        # get_tree(post_lst[root_index:-1], in_lst[root_index+1:])
        return root


"""封装重建树"""


class ReTree(Tree):

    def __init__(self, node=None):
        super().__init__(node)

    def re_tree(self, pre_lst, in_lst):
        """接收前序和中序遍历结果的列表，返回后序遍历结果的列表"""
        if not pre_lst:
            return
        else:
            self.root = Node(pre_lst[0])
            root_index = in_lst.index(pre_lst[0])
            self.root.left_child = ReTree(self.root.left_child).re_tree(
                pre_lst[1:root_index+1], in_lst[:root_index])
            self.root.right_child = ReTree(self.root.right_child).re_tree(
                pre_lst[root_index+1:], in_lst[root_index+1:])
            return self.root


if __name__ == '__main__':
    pre_lst = [1, 2, 4, 7, 3, 5, 6, 8]
    in_lst = [4, 7, 2, 1, 5, 3, 8, 6]
    pre_lst2 = [1, 2, 3, 5, 6, 4]
    in_lst2 = [5, 3, 6, 2, 4, 1]
    tree = ReTree()
    tree.re_tree(pre_lst, in_lst)
    tree2 = ReTree()
    tree2.root = get_tree(pre_lst2, in_lst2)
    for tr in [tree, tree2]:
        tr.preorder()
        print("")
        tr.inorder()
        print("")
        tr.postorder()
        print("\n{:-^20}".format("封装"))


