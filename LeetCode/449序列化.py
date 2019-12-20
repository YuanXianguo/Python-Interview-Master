class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "#"
        return "{},{},{}".format(root.val, self.serialize(root.left), self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.index = -1
        self.datas = data.split(",")
        return self.main()

    def main(self):
        self.index += 1
        if self.index > len(self.datas):
            return
        root = None
        if self.datas[self.index] != "#":
            root = TreeNode(int(self.datas[self.index]))
            root.left = self.main()
            root.right = self.main()
        return root

