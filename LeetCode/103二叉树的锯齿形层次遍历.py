def zigzagLevelOrder(root):
    if not root:
        return []
    from collections import deque
    q1 = deque()
    q2 = deque()
    res = []
    q1.append(root)
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
            res.append(tmp[::-1])
    return res


