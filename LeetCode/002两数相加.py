"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addt(l1, l2):
    flag = 0  # 判断是否进位
    dummy = ListNode(0)  # 定义哑点
    tmp = dummy  # 定义临时结点
    while l1 or l2:
        # 取出l1，l2值，并分别移动一位（如果存在）
        if l1:
            val1 = l1.val
            l1 = l1.next
        else:
            val1 = 0
        if l2:
            val2 = l2.val
            l2 = l2.next
        else:
            val2 = 0
        # 创建结点存储计算结果
        node = ListNode(0)
        node.val = val1 + val2 + flag
        flag = 0  # 重置flag
        if node.val >= 10:  # 判断进位
            node.val %= 10
            flag = 1
        tmp.next = node
        tmp = tmp.next
    if flag:  # 循环最后一次的flag还没判断
        node = ListNode(1)
        tmp.next = node
    return dummy.next


def addTwoNumbers(l1, l2):
    flag = 0  # 判断是否进位
    l1_pre = None  # 记录链表1当前结点的前一个结点，用于拼接链表2
    head = l1  # 将计算结果存储到链表1，返回链表1头结点
    while l1 and l2:  # 链表1和链表2都不为空
        l1.val = l1.val + l2.val + flag
        flag = 0
        if l1.val >= 10:
            l1.val = l1.val % 10
            flag = 1
        l1_pre = l1
        l1 = l1.next
        l2 = l2.next
    if not l1 and not l2:  # 链表1和链表2同时变量完
        if flag:  # 如果遍历结束还需要进位，就创建一个新结点，并通过pre添加到结果链表中
            node = ListNode(1)
            l1_pre.next = node
    elif not l2:  # 链表2先变量完
        pre = None
        while flag and l1:
            l1.val += flag
            flag = 0
            if l1.val == 10:
                l1.val = 0
                flag = 1
            pre = l1
            l1 = l1.next
        if flag:
            node = ListNode(1)
            pre.next = node
    elif not l1:  # 变量1先遍历完
        l1_pre.next = l2  # 剩余部分结果存储在链表2中，并将链表2拼接到链表1
        pre = None
        while flag and l2:
            l2.val += flag
            flag = 0
            if l2.val == 10:
                l2.val = 0
                flag = 1
            pre = l2
            l2 = l2.next
        if flag:
            node = ListNode(1)
            pre.next = node
    return head  # 返回链表1头结点


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        flag = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + flag
            if sum_val >= 10:
                sum_val %= 10
                flag = 1
            else:
                flag = 0
            head.next = ListNode(sum_val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum_val = l1.val + flag
            if sum_val >= 10:
                sum_val %= 10
                flag = 1
            else:
                flag = 0
            head.next = ListNode(sum_val)
            head = head.next
            l1 = l1.next
        while l2:
            sum_val = l2.val + flag
            if sum_val >= 10:
                sum_val %= 10
                flag = 1
            else:
                flag = 0
            head.next = ListNode(sum_val)
            head = head.next
            l2 = l2.next
        if flag:
            head.next = ListNode(1)
        return dummy.next


if __name__ == '__main__':
    from single_link_list import SingleLinkList
    s1 = SingleLinkList()
    s2 = SingleLinkList()
    for i in range(1,2):
        s1.add_rear(i)
    s2.add_rear(9)
    s2.add_rear(9)

    # s = SingleLinkList(addTwoNumbers(s1.head, s2.head))
    s = SingleLinkList(addt(s1.head, s2.head))
    s.travel()

