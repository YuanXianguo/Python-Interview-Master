from sword_offer.tree import Tree


class Node(object):
    """结点"""
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(Tree):
    """二叉搜索树"""
    def __init__(self, node=None):
        super().__init__(node)

    def insert(self, val):
        """二叉搜索树插入"""
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            if val < self.root.val:
                self.root.left = BinarySearchTree(
                    self.root.left).insert(val)
            elif val > self.root.val:
                self.root.right = BinarySearchTree(
                    self.root.right).insert(val)
        return self.root

    def find(self, val):
        """递归查找值"""
        if not self.root:
            return "查找失败"
        if val < self.root.val:
            return BinarySearchTree(self.root.left).find(val)
        elif val > self.root.val:
            return BinarySearchTree(self.root.right).find(val)
        else:  # 找到了
            return self.root

    def find2(self, val):
        """非递归查找"""
        root = self.root
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return "查找失败"

    def find_min(self):
        """递归查找最小值，一定是在树的最左分支的端结点上"""
        if not self.root:
            return "查找失败"
        if not self.root.left:
            return self.root  # 最小值没有左子树
        else:
            return BinarySearchTree(self.root.left).find_min()

    def find_max(self):
        """迭代查找最大值，一定是在树的最右分支的端结点上"""
        root = self.root
        if not root:
            return "查找失败"
        while root.right:
            root = root.right
        return root

    def delete(self, val):
        """每次递归删除都把删除后的子树返回"""
        if not self.root:
            return "删除失败"
        elif val < self.root.val:
            self.root.left = BinarySearchTree(
                self.root.left).delete(val)
        elif val > self.root.val:
            self.root.right = BinarySearchTree(
                self.root.right).delete(val)
        else:  # 该结点为要删除结点
            # 如果左右子树都不为空
            if self.root.left and self.root.right:
                # 找到右子树最小值或左子树最大值
                right_min = BinarySearchTree(self.root.right).find_min()
                # 将找到的右子树最小值填充要删除的根结点
                self.root.val = right_min.val
                # 删除右子树最小值
                self.root.right = BinarySearchTree(
                    self.root.right).delete(right_min)
            else:  # 被删除结点有一个或无子树
                if not self.root.left:
                    self.root = self.root.right
                elif not self.root.right:
                    self.root = self.root.left
        return self.root


if __name__ == '__main__':
    bt = BinarySearchTree()
    for i in range(10):
        bt.insert(i)
    print(bt.find_min().val)
    print(bt.find_max().val)
    print(bt.find(10))
    bt.postorder()
    print("")
    bt.delete(9)
    print(bt.find_max().val)

    bt.inorder()
