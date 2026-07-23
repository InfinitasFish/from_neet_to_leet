from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # recursion? reordered list is first + last element
        #   and reordered list between them

        # base case
        if head is None or head.next is None:
            return

        first = head
        # get to last element and before last element, to break a link
        bLast = None
        while head.next is not None:
            bLast = head
            head = head.next

        # get element for next step of recursion
        next = first.next

        # assign first element to last
        first.next = head

        # break a link between last and before last elements before recursion
        if id(bLast.next) != id(next):
            bLast.next = None
        else:
            return

        # assign last to element after first, to not lost elements
        head.next = next
        self.reorderList(next)


if __name__ == "__main__":
    s = Solution()
    t1 = ListNode(1, ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10))))))
    s.reorderList(t1)

    print('[', end='')
    while t1:
        print(t1.val, end=", ")
        t1 = t1.next
    print(']')

    t1 = ListNode(1, ListNode(2, ListNode(4, ListNode(6, ListNode(8, None)))))
    s.reorderList(t1)

    print('[', end='')
    while t1:
        print(t1.val, end=", ")
        t1 = t1.next
    print(']')
