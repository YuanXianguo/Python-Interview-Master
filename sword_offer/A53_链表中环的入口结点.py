"""
题目：一个链表中包含环，请找出该链表的环的入口结点。
"""
from sword_offer.single_link_list import SingleLinkList


def find_entrance(head):
    if not head:
        return
    stack = []
    while head:
        if head not in stack:
            stack.append(head)
            head = head.next
        else:
            return head


def get_ll():
    ll = SingleLinkList()
    for i in range(10):
        ll.add_rear(i)
    head = ll.head
    stack = []
    while head:
        stack.append(head)
        head = head.next
    stack[5].next = stack[1]
    print(find_entrance(ll.head).elem)


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return
        slow = pHead.next
        fast = pHead.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        # 第一次相遇时慢指针走了环长，第二次相遇时快指针指向环入口
        fast = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast


if __name__ == '__main__':
    get_ll()
