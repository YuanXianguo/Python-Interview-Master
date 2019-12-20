"""
题目：输入两个单调递增的链表，输出两个链表合成后的链表，需要满足单调不减规则。
"""
from collections import deque
from sword_offer.single_link_list import SingleLinkList, Node


def merge_sll_queue(sll1, sll2):
    """用两个指针将两个链表依次比较，按不减规则放入队列，然后组成新链表"""
    q = deque()  # 创建队列
    cursor1 = sll1.head
    cursor2 = sll2.head
    while cursor1 and cursor2:  # 两个指针都不为空进入循环
        if cursor1.elem <= cursor2.elem:
            q.append(cursor1)
            cursor1 = cursor1.next
        else:
            q.append(cursor2)
            cursor2 = cursor2.next
    if cursor1:  # 如果链表1不为空，将未放入队列的第一个结点放入队列
        q.append(cursor1)
    elif cursor2:
        q.append(cursor2)
    sll1.head = q.popleft()
    cursor = sll1.head
    while q:
        cursor.next = q.popleft()
        cursor = cursor.next
    return sll1


def merge_sll_iter(head1, head2):
    """新建一个链表，依次存放不减结点"""
    node = Node(0)
    head = node

    while head1 and head2:
        if head1.elem <= head2.elem:
            node.next = head1
            head1 = head1.next
        else:
            node.next = head2
            head2 = head2.next
        node = node.next
    if head1:
        node.next = head1
    elif head2:
        node.next = head2
    return head.next


def merge_sll_digui(head1, head2):
    """采用递归"""
    if not head1:  # 链表1为空，返回链表2
        return head2
    if not head2:  # 链表2为空，返回链表1
        return head1
    if head1.elem <= head2.elem:
        head = head1
        head.next = merge_sll_digui(head1.next, head2)
    else:
        head = head2
        head.next = merge_sll_digui(head1, head2.next)
    return head


if __name__ == '__main__':
    print("{:-^50}".format("新建队列法"))
    sll1 = SingleLinkList()
    sll2 = SingleLinkList()
    for i in range(10):
        sll1.add_rear(2*i)
        sll2.add_rear(2*i+1)
    sll1.travel()
    sll2.travel()
    sll = merge_sll_queue(sll1, sll2)
    sll.travel()

    print("{:-^50}".format("新建链表法"))
    sll3 = SingleLinkList()
    sll4 = SingleLinkList()
    for i in range(10):
        sll3.add_rear(2*i)
        sll4.add_rear(2*i+1)
    sll3.travel()
    sll4.travel()
    head = merge_sll_iter(sll3.head, sll4.head)
    sll_ = SingleLinkList(head)
    sll_.travel()

    print("{:-^50}".format("递归法"))
    sll5 = SingleLinkList()
    sll6 = SingleLinkList()
    for i in range(10):
        sll5.add_rear(2*i)
        sll6.add_rear(2*i+1)
    sll5.travel()
    sll6.travel()
    head = merge_sll_iter(sll5.head, sll6.head)
    sll_ = SingleLinkList(head)
    sll_.travel()
