"""
题目：请实现两个函数，分别用来序列化和反序列化二叉树。
"""
from sword_offer.binary_serach_tree import BinarySearchTree, Node


class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return "#"
        return "{},{},{}".format(root.val, self.Serialize(root.left), self.Serialize(root.right))

    def Deserialize(self, s):
        # write code here
        self.index = -1
        ls = s.split(",")

        def des_main():
            self.index += 1
            if self.index >= len(ls):
                return
            root = None
            if ls[self.index] != "#":
                root = Node(int(ls[self.index]))
                root.left =des_main()
                root.right = des_main()
            return root
        return des_main()


def des(string):
    if not string:
        return
    index = -1
    ls = string.split(",")

    def inner():
        nonlocal index
        index += 1
        if index > len(ls):
            return
        root = None
        if ls[index] != "#":
            root = Node(int(ls[index]))
            root.left = inner()
            root.right = inner()
        return root
    return inner()


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(10):
        bst.add(i)
    s = Solution()
    string = s.Serialize(bst.root)
    print(string)
    # root = s.Deserialize(string)
    root = des(string)
    new_t = BinarySearchTree(root)
    string = s.Serialize(new_t.root)
    print(string)
