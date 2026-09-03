from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # critical point - local maxima or minima
        # local here means compared to two neighbor nodes

        critical_ids = []
        cur = head
        prev = None
        count = 0
        while cur:
            if prev is not None and cur.next is not None:
                if prev.val < cur.val > cur.next.val:
                    critical_ids.append(count)
                elif prev.val > cur.val < cur.next.val:
                    critical_ids.append(count)

            prev = cur
            cur = cur.next
            count += 1

        if len(critical_ids) < 2:
            return [-1, -1]

        # passes, but we can optimize this by calculating min/max dists while iterating through linked list
        max_dist = critical_ids[-1] - critical_ids[0]
        min_dist = min(critical_ids[i] - critical_ids[i - 1] for i in range(1, len(critical_ids)))

        return [min_dist, max_dist]


s = Solution()
head = ListNode(3, ListNode(1))
print(s.nodesBetweenCriticalPoints(head))  # [-1, -1]
head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
print(s.nodesBetweenCriticalPoints(head))  # [1, 3]
head = ListNode(3, ListNode(5, ListNode(3, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(1))))))))
print(s.nodesBetweenCriticalPoints(head))  # [2, 5]



