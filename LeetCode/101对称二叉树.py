class Solution:
    def isSymmetric(self, root):

        def is_sym_main(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return is_sym_main(root1.left, root2.right) and is_sym_main(root1.right, root2.left)
        return is_sym_main(root, root)


class Solution2:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        stack = [root.left, root.right]
        while stack:
            left = stack.pop()
            right = stack.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val == right.val:
                stack.append(left.right)
                stack.append(right.left)
                stack.append(left.left)
                stack.append(right.right)
            else:
                return False
        return True
