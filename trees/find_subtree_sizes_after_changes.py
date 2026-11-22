from __future__ import annotations
from collections import defaultdict


class Solution_:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        tree = [[] for _ in range(n)]
        ans = [n] * n
        # keep the nearest matching ancestor
        last = [-1] * 26

        # collect connections from parents to nodes
        for i in range(1, n):
            adj[parent[i]].append(i)

        def dfs(u):
            c = ord(s[u]) - ord('a')
            old = last[c]

            # if matching ancestor exists, update the
            # current node's parent
            if u and old != -1:
                parent[u] = old
            last[c] = u

            for v in adj[u]:
                dfs(v)

            # restore the previous `last[c]`
            # to maintain the correct DFS path
            last[c] = old

        # calculate the subtree size for updated `parent`
        def calc(u):
            ans[u] = 1
            for v in tree[u]:
                ans[u] += calc(v)
            return ans[u]

        dfs(0)

        for i in range(1, n):
            tree[parent[i]].append(i)

        calc(0)
        return ans


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # previous solution is not mine, so let's make a new one
        N = len(parent)
        # adjacency list
        parent_to_nodes = defaultdict(list)
        # character to idx of last occurrence
        last_occur = {}
        # result with updated subtree sizes
        res = [-1] * N

        for i in range(1, N):
            parent_to_nodes[parent[i]].append(i)

        # traversal can be pre- or post-order
        # e.x in [-1,0,0,1,1,1] and [0,1,2,3,4,5] case
        # pre-order: 0,1,3,4,5,2
        # post-order: 3,4,5,1,2,0
        # our dfs will apply both for `last_occur`, adding occurrences in pre-order
        # and removing them in post-order
        # this way we can accurately simulate the structure of the tree
        # without making unexisting connections
        def dfs(node_idx):
            char_num = ord(s[node_idx]) - ord('a')
            last_idx = last_occur.get(char_num, -1)
            # if we've seen this character earlier, we found new parent
            if last_idx != -1:
                parent[node_idx] = last_idx

            # add current node into map in pre-order
            last_occur[char_num] = node_idx

            # do new parent search in each node below
            for child_idx in parent_to_nodes[node_idx]:
                dfs(child_idx)

            # going back up in the tree,
            # so remove current node from map in post-order,
            # assign to previous occurrence instead
            last_occur[char_num] = last_idx

        dfs(0)

        # after updating parents, we need to make a new tree before calculating result
        tree = defaultdict(list)
        for i in range(N):
            tree[parent[i]].append(i)

        # calculate result, assign size `1` in pre-order and finalize size in post-order
        def calc_size(node_idx):
            curr_size = 1
            for child_idx in tree[node_idx]:
                curr_size += calc_size(child_idx)

            res[node_idx] = curr_size
            return curr_size

        calc_size(0)
        return res


s = Solution()
print(s.findSubtreeSizes([-1,0,0,1,1,1], "abaabc"))  # [6,3,1,1,1,1]
