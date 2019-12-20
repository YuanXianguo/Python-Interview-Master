from sword_offer.single_link_list import SingleLinkList


def get_first_same_node(head1, head2):
    len1 = get_length(head1)
    len2 = get_length(head2)
    while head1:
        if len1 > len2:
            while len1 > len2:
                head1 = head1.next
                len1 -= 1
        elif len1 < len2:
            while len1 < len2:
                head2 = head2.next
                len2 -= 1
        if head1.elem == head2.elem:
            return head1
        head1 = head1.next
        head2 = head2.next


def get_length(head):
    cnt = 0
    while head:
        head = head.next
        cnt += 1
    return cnt


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = self.get_length(pHead1)
        len2 = self.get_length(pHead2)
        if len1 < len2:
            while len2 > len1:
                pHead2 = pHead2.next
                len2 -= 1
        elif len1 > len2:
            while len2 < len1:
                pHead1 = pHead1.next
                len1 -= 1
        while pHead1 and pHead1.val != pHead2.val:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1

    def get_length(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt


if __name__ == '__main__':
    ssl1 = SingleLinkList()
    for i in range(10):
        ssl1.add_rear(i)
    ssl2 = SingleLinkList()
    for i in range(5, 10):
        ssl2.add_rear(i)
    print(get_first_same_node(ssl1.head, ssl2.head).elem)
