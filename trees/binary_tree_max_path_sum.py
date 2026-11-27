from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # brute-force TLE
        # collecting values in inorder traversal
        # if we want to take n0 and n5, we will have to take everything between them
        # so we can check sums of windows of all sizes from 1 to len(vals)

        if root is None:
            return 0

        max_sum = -float("inf")
        inorder_vals = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            inorder_vals.append(node.val)
            inorder(node.right)

        inorder(root)

        n = len(inorder_vals)
        for size in range(1, n + 1):
            for i in range(n - size + 1):
                max_sum = max(max_sum, sum(inorder_vals[i:i+size]))

        return max_sum




s = Solution_()
root = TreeNode(-15, TreeNode(10), TreeNode(20, TreeNode(15, TreeNode(-5)), TreeNode(5)))
print(s.maxPathSum(root))  # 40
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.maxPathSum(root))  # 6