from __future__ import annotations


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution_:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # four pass is TLE expectedly
        if head == None:
            return None

        # am I dum-dum?
        ll = []
        cur = head
        while cur is not None:
            ll.append(cur)
            cur = cur.next

        rl = []
        cur = head
        while cur is not None:
            if cur.random is not None:
                rl.append(ll.index(cur.random))
            else:
                rl.append(None)
            cur = cur.next

        copy_head = Node(head.val, None, None)
        ll_copy = [copy_head]
        cur_copy = copy_head
        for i in range(1, len(ll)):
            cur_copy.next = Node(ll[i].val, None, None)
            cur_copy = cur_copy.next
            ll_copy.append(cur_copy)

        for i in range(len(rl)):
            if rl[i] is not None:
                ll_copy[i].random = ll_copy[rl[i]]

        return copy_head


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # well it was a hashmap all along
        oldToCopy = {None: None}

        cur = head
        while cur is not None:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur is not None:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


s = Solution()
nodes = [Node(3), Node(7), Node(4), Node(5)]
head = nodes[0]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
nodes[1].random = nodes[2]
nodes[2].random = nodes[2]
print(s.copyRandomList(head))
