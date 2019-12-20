"""
题目：输入一个链表，输出该链表中倒数第k个结点。
"""
from sword_offer.single_link_list import SingleLinkList


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not k or not head:
            return
        stack = list()
        while head:
            stack.append(head)
            head = head.next
        while k > 1 and stack:
            stack.pop()
            k -= 1
        if stack:
            return stack.pop()


if __name__ == '__main__':
    sll = SingleLinkList()
    for i in range(10):
        sll.add_rear(i)

