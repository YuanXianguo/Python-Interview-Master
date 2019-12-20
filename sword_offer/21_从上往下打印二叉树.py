from sword_offer.binary_serach_tree import BinarySearchTree


def travel_level(root):
    if not root:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.elem, end=" ")
        if node.left_child:
            queue.append(node.left_child)
        if node.right_child:
            queue.append(node.right_child)


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(10):
        bst.add(i)

    travel_level(bst.root)
