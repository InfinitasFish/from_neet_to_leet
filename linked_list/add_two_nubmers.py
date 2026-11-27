from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution__:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # slow somewhy

        if not l1 and not l2:
            return ListNode()

        pairs = []
        while l1 and l2:
            pairs.append((l1.val, l2.val))
            l1 = l1.next
            l2 = l2.next

        while l1:
            pairs.append((l1.val, 0))
            l1 = l1.next

        while l2:
            pairs.append((0, l2.val))
            l2 = l2.next

        sums = []
        f = False
        for v1, v2 in pairs:
            sum = v1 + v2 + int(f)
            if sum >= 10:
                f = True
            else:
                f = False
            sums.append(sum % 10)

        if f:
            sums.append(1)

        res = ListNode()
        cur = res
        for i, val in enumerate(sums):
            cur.val = val

            if i != len(sums) - 1:
                cur.next = ListNode()
                cur = cur.next

        return res


class Solution_:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive, fastest (some why)
        if not l1 and not l2:
            return ListNode()

        def add(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_ = v1 + v2 + carry
            res = ListNode(sum_ % 10)
            next_node = add(l1.next if l1 else None, l2.next if l2 else None, 1 if sum_ >= 10 else 0)
            res.next = next_node

            return res

        r = add(l1, l2, 0)
        return r


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # simple iteration, slower than recursion
        if not l1 and not l2:
            return ListNode()

        res = ListNode()
        dummy = res
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_ = v1 + v2 + carry
            carry = sum_ >= 10
            dummy.next = ListNode(sum_ % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next

        return res.next


s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(4, ListNode(5, ListNode(6)))
#print(s.addTwoNumbers(list1, list2))  # [5,8,0]
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(4, ListNode(5, ListNode(6)))
#print(s.addTwoNumbers(list1, list2))  # [5,7,9]
list1 = ListNode(9)
list2 = ListNode(9, ListNode(9))
print(s.addTwoNumbers(list1, list2))  # [8, 0, 1]