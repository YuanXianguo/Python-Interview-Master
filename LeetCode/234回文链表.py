"""
请判断一个链表是否为回文链表。
"""


def isPalindrome(head):
    tmp = []
    while head:
        tmp.append(head.val)
        head = head.next
    if len(tmp) == 1:
        return True
    for i in range(len(tmp)//2):
        if tmp[i] != tmp[-(i+1)]:
            return False
    return True


def isPalindrome2(head):
    if not head or not head.next:
        return True
    # 通过快慢指针找到链表中点
    slow = head
    fast = head
    # 每次循环快指针遍历2个结点，慢指针遍历1个结点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow  # 找到中点结点
    pre = None
    while slow:  # 后半段链表反转
        slow.next, pre, slow = pre, slow, slow.next
    # 反转后半段链表的头结点为pre，前半段链表的头结点为head
    while head != mid:  # 同时遍历两半段链表，直到中点；
        if head.val != pre.val:
            return False
        head = head.next
        pre = pre.next
    return True


if __name__ == '__main__':
    from single_link_list import SingleLinkList
    sll = SingleLinkList()
    for i in range(4):
        sll.add_rear(i)
    for i in range(3, -1, -1):
        sll.add_rear(i)
    sll.travel()
    print(isPalindrome(sll.head))
    print(isPalindrome2(sll.head))
