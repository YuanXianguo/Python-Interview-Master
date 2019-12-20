def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


if __name__ == '__main__':
    from tree import Tree
    t = Tree()
    for i in range(10):
        t.add(i)
    print(get_height(t.root))
