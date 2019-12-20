def reverse_list(head):
    pre = None
    while head:
        pre_pre = pre
        pre = head
        head = head.next
        pre.next = pre_pre
    return pre


def reverse2(head):
    pre = None
    while head:
        head.next, pre, head = pre, head, head.next
    return pre


if __name__ == '__main__':
    from single_link_list import SingleLinkList
    ssl = SingleLinkList()
    for i in range(2):
        ssl.add_rear(i)
    ssl.travel()
    head = reverse_list(ssl.head)
    ssl2 = SingleLinkList(head)
    ssl2.travel()

    ss3 = SingleLinkList()
    for i in range(5):
        ss3.add_rear(i)
    ss3.travel()
    head = reverse2(ss3.head)
    ss4 = SingleLinkList(head)
    ss4.travel()
