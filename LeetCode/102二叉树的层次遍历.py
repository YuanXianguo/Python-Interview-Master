def levelOrder(root):
    if not root:
        return []
    from collections import deque
    q1 = deque()
    q1.append(root)
    q2 = deque()
    res = []
    while q1 or q2:
        tmp = []
        while q1:
            node = q1.popleft()
            if node.val is not None:
                tmp.append(node.val)
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        if tmp:
            res.append(tmp)
        tmp = []
        while q2:
            node = q2.popleft()
            if node.val is not None:
                tmp.append(node.val)
            if node.left:
                q1.append(node.left)
            if node.right:
                q1.append(node.right)
        if tmp:
            res.append(tmp)
    return res


if __name__ == '__main__':
    from tree import Tree
    t = Tree()
    for i in [3,9,20,None,None,15,7]:
        t.add(i)
    print(levelOrder(t.root))
