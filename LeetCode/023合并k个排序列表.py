"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""


from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        head = dummy = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            head.next = node
            head = head.next
            node = node.next
            if node:
                q.put((node.val, node))
        return dummy.next


class Solution2:
    def mergeKLists(self, lists):
        if not lists:
            return
        while len(lists) >= 2:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lmerge2 = self.merge2Lists(l1, l2)
            lists.append(lmerge2)
        return lists.pop()

    def merge2Lists(self, l1, l2):
        head = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next, l1 = l1, l1.next
            else:
                head.next, l2 = l2, l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next
