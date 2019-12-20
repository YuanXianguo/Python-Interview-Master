def getIntersectionNode(self, headA, headB):

    def get_length(head):
        if not head:
            return 0
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    la = get_length(headA)
    lb = get_length(headB)

    if la > lb:
        dif = la - lb
        while dif:
            headA = headA.next
            dif -= 1
    else:
        dif = lb - la
        while dif:
            headB = headB.next
            dif -= 1
    while headA:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        lenA = self.get_length(headA)
        lenB = self.get_length(headB)
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

    def get_length(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt


class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha


