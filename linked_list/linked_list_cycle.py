from __future__ import annotations


class Solution:
    # easy problem, using set of nodes ids, see the same node -> there's a cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head is not None:
            if id(head) in visited:
                return True
            visited.add(id(head))
            head = head.next

        return False
