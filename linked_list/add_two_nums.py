from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        ten = False
        while l1 or l2:
            v1 = 0
            v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            sum = v1 + v2 + int(ten)
            ten = True if sum >= 10 else False
            head.val = sum % 10

            if l1 or l2:
                head.next = ListNode()
                head = head.next

        if ten:
            head.next = ListNode()
            head.val = 1

        return result


if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(s.addTwoNumbers(l1, l2))  # 708