"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
from single_link_list import SingleLinkList, ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        """递归"""
        if not l1:  # 如果l1为空，返回l2（可为空）
            return l2
        if not l2:  # 如果l1不为空，l2为空，返回l1
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution2:
    def mergeTwoLists(self, l1, l2):
        """迭代"""
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:  # l1,l2都不空，把值小的结点添加到新链表头后面
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if not l1:  # l1空
            tmp.next = l2
        else:
            tmp.next = l1
        return dummy.next
