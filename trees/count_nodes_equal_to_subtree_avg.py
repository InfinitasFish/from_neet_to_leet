from __future__ import annotations
from math import floor


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        # sum, count, avgs
        def dfs(leaf):
            if leaf is None:
                return 0, 0, 0

            left = dfs(leaf.left)
            right = dfs(leaf.right)
            sum = left[0] + right[0] + leaf.val
            count = left[1] + right[1] + 1
            avgs = left[2] + right[2]
            if count > 0 and floor(sum / count) == leaf.val:
                return sum, count, avgs + 1

            return sum, count, avgs

        return dfs(root)[2]


s = Solution()
t = TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))
print(s.averageOfSubtree(t))  # 5


