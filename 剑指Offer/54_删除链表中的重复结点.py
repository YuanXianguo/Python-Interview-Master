"""
题目：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
"""
from sword_offer.single_link_list import SingleLinkList


class ListNode:
    def __init__(self, x):
            self.elem = x
            self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        tmp = {}
        node = pHead
        while node:
            if node.elem in tmp:
                tmp[node.elem] = 2
            else:
                tmp[node.elem] = 1
            node = node.next
        lst = []
        for key, value in tmp.items():
            if value == 1:
                lst.append(key)
        lst.sort()
        if not lst:
            return
        head = pre = ListNode(lst.pop(0))
        while lst:
            node = ListNode(lst.pop(0))
            pre.next = node
            pre = node
        return head


class Solution0:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return
        dummy = ListNode(0)
        dummy.next = pHead
        pre = dummy
        tmp = pHead
        pHead = pHead.next
        while pHead:
            if pHead.val == tmp.val:
                pre.next = pHead.next
            else:
                tmp = pHead
                if pHead.next and pHead.next.val != pHead.val:
                    pre = pHead
            pHead = pHead.next
        return dummy.next


class Solution2:
    def deleteDuplication(self, pHead):
        last = dummy = ListNode(0)
        tmp = node = dummy.next = pHead
        node = node.next
        while node:
            if node.val == tmp.val:
                last.next = node.next
            else:
                tmp = node
                if node.next and node.next.val != node.val:
                    last = node
            node = node.next
        return dummy.next


if __name__ == '__main__':
    sll = SingleLinkList()
    sll.add_rear(1)
    sll.add_rear(1)
    sll.add_rear(2)
    sll.add_rear(3)
    s = Solution()
    head = s.deleteDuplication(sll.head)
    sl = SingleLinkList(head)
    sl.travel()
