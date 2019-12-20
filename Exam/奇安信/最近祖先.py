n = int(input())
nums = list(map(int, input().split()))
a12 = input().split()
a1, a2 = int(a12[0]), int(a12[1])


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, node=None):
        self.root = node

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.left)
                queue.append(cur_node.right)


def common(root, p, q):
    if p > q:
        p, q = q, p
    while root:
        if root.val > q:
            root = root.left
        elif root.val < p:
            root = root.right
        else:
            return root.val
    return -1


tree = Tree()
for i in nums:
    tree.add(i)

print(common(tree.root, a1, a2))
