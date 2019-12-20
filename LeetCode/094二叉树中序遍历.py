from tree import Tree


def inorderTraversal(root):
    res = []
    stack = []
    while root or len(stack):  # 如果当前结点不空或堆栈不空，循环指向下两步
        while root:  # 将结点左子树全部压栈
            stack.append(root)
            root = root.left
        if len(stack):  # 如果栈不为空则弹出栈顶元素并将其加入遍历结果
            root = stack.pop()
            res.append(root.val)
            root = root.right  # 指向当前结点右子树
    return res


if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
    print(inorderTraversal(t.root))
