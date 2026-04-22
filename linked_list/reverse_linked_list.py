from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = head
        next_node = head.next
        new_head.next = None
        while next_node:
            temp = next_node.next
            next_node.next = new_head
            new_head = next_node
            next_node = temp

        return new_head


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
rev_head = Solution().reverseList(head)
while rev_head:
    print(rev_head.val, end=" ")
    rev_head = rev_head.next

