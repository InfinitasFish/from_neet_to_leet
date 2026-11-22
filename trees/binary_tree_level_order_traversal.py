from __future__ import annotations
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        # instead of map we can keep list and add `[]` each time we hit a new level
        levels = defaultdict(list)
        levels[0].append(root.val)

        def dfs(node, level):
            if node is None:
                return

            # to keep target order from left to right, first go to left node, then to right node
            levels[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        # target left to right order
        dfs(root.left, 1)
        dfs(root.right, 1)

        # drop keys and return list of lists
        return [nodes for nodes in levels.values()]


class Solution_:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # previous solution uses depth-first traversal,
        # but we also can do breath-first approach
        # to make this possible, we have to use queue
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            # each iteration - one level
            # keep `len` in variable because queue will be updated within iteration
            q_len = len(queue)
            for i in range(q_len):
                node = queue.popleft()
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if level:
                res.append(level)

        return res


s = Solution_()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)))
print(s.levelOrder(root))  # [[1], [2, 3], [4, 5, 6, 7]]
root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))),
                TreeNode(3, None, TreeNode(5, TreeNode(7))))
print(s.levelOrder(root))  # [[1], [2, 3], [4, 5], [6, 7]]
