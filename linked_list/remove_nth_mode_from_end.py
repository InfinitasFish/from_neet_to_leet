from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None

        size = 0
        curr = head
        while curr is not None:
            curr = curr.next
            size += 1
        if n > size:
            return head
        elif n == size:
            return head.next

        n_ = size - n
        curr = head
        while n_ > 1:
            curr = curr.next
            n_ -= 1

        after = curr.next.next
        curr.next = after

        return head


s = Solution()
print(s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2))  # [1,2,4]

