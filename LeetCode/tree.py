class Node(object):
    """结点"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    """二叉树"""

    def __init__(self, node=None):
        self.root = node

    def add(self, val):
        """层序添加"""
        node = Node(val)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node.left:  # 如果左子树为空
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            else:    # 如果左右子树都不为空，压进堆栈，判断子树的子树
                queue.append(cur_node.left)
                queue.append(cur_node.right)

    def breadth_travel(self):
        """广度遍历，层序遍历"""
        if not self.root:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=" ")
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        print("")

    def preorder(self):
        """先序遍历"""
        if not self.root:
            return
        print(self.root.val, end=" ")
        Tree(self.root.left).preorder()
        Tree(self.root.right).preorder()

    def inorder(self):
        """中序遍历"""
        if not self.root:
            return
        Tree(self.root.left).inorder()
        print(self.root.val, end=" ")
        Tree(self.root.right).inorder()

    def postorder(self):
        """后序遍历"""
        if not self.root:
            return
        Tree(self.root.left).postorder()
        Tree(self.root.right).postorder()
        print(self.root.val, end=" ")

    def get_height(self):
        """求二叉树高度"""
        if self.root:
            hl = Tree(self.root.left).get_height()
            hr = Tree(self.root.right).get_height()
            return max(hl, hr) + 1
        else:
            return 0


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    tree.breadth_travel()
    tree.preorder()
    print("")
    tree.inorder()
    print("")
    tree.postorder()
    print("")
    print(tree.get_height())
