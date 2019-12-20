"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""
from single_link_list import SingleLinkList, ListNode


def removeNthFromEnd(head, n):
    dic = {}
    flag = 0
    while head:
        dic[flag] = head
        head = head.next
        flag += 1
    if flag - n == 0:  # 如果删除头结点
        if 1 in dic:  # 如果有超过两个结点，将第二个结点返回作为新头结点
            return dic[1]
        return None  # 如果只有一个结点，则返回空
    # 如果要删除的结点的下一个结点存在，则将当前结点的上一个结点指向下一个结点
    if flag - n + 1 in dic:
        dic[flag - n - 1].next = dic[flag - n + 1]
    else:  # 如果删除的是尾结点，则将尾结点的上一个结点的next置为空
        dic[flag - n - 1].next = None
    return dic[0]  # 返回原头结点


def remove2(head, n):
    """快慢指针"""
    dummy = ListNode(0)  # 定义一个哑点，以处理极端情况，如删除的是头结点
    dummy.next = head
    cursor1, cursor2 = dummy, dummy
    cnt = 0
    # 快指针向前移动n+1位，此时快指针指向n+1，慢指针指向0，被n个结点分开（没有哑点就是（1，n+2））
    while cnt <= n:
        cursor1 = cursor1.next
        cnt += 1
    while cursor1:  # 当快指针指向None时，慢指针指向-(n+1)结点
        cursor1 = cursor1.next
        cursor2 = cursor2.next
    cursor2.next = cursor2.next.next  # 当前慢指针指向-(n+1)
    return dummy.next


def remove3(head, n):
    """快慢指针"""
    # dummy = ListNode(0)  # 定义一个哑点，以处理极端情况，如删除的是头结点
    # dummy.next = head
    if n == 1:
        return head.next
    cursor1, cursor2 = head, head
    cnt = 0
    # 快指针向前移动n+1位，此时快指针指向n+1，慢指针指向0，被n个结点分开（没有哑点就是（1，n+2））
    while cnt <= n:
        cursor1 = cursor1.next
        cnt += 1
    while cursor1:  # 当快指针指向None时，慢指针指向-(n+1)结点
        cursor1 = cursor1.next
        cursor2 = cursor2.next
    cursor2.next = cursor2.next.next  # 当前慢指针指向-(n+1)
    return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    sll = SingleLinkList()
    for i in range(2):
        sll.add_rear(i+1)
    new_sll = SingleLinkList(removeNthFromEnd(sll.head, 1))
    new_sll.travel()

    sll2 = SingleLinkList()
    for i in range(2):
        sll2.add_rear(i+1)
    ns = SingleLinkList(remove2(sll2.head, 2))
    ns.travel()

    sll3 = SingleLinkList()
    for i in range(2):
        sll3.add_rear(i+1)
    ns = SingleLinkList(remove3(sll3.head, 1))
    ns.travel()
