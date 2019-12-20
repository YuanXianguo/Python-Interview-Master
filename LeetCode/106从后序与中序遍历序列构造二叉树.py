class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(inorder, postorder):
    if not postorder:
        return None
    root = TreeNode(postorder[-1])
    root_index = inorder.index(root.val)
    post_left = postorder[:root_index]
    post_right = postorder[root_index:-1]
    in_left = inorder[:root_index]
    in_right = inorder[root_index+1:]
    root.left = buildTree(in_left, post_left)
    root.right = buildTree(in_right, post_right)
    return root
