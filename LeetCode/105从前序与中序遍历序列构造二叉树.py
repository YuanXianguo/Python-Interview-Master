class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    root_index = inorder.index(root.val)
    pre_left = preorder[1: root_index + 1]
    pre_right = preorder[root_index + 1:]
    in_left = inorder[:root_index]
    in_right = inorder[root_index + 1:]
    root.left = buildTree(pre_left, in_left)
    root.right = buildTree(pre_right, in_right)
    return root
