def has_cycle(head):
    """采用快慢指针法，如果存在环，则快慢指针会在环内相遇"""
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
