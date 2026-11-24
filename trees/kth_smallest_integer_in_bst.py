from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # trivial
        def dfs(node, vals):
            if node is None:
                return

            # go to the bottom of left, then add current, then add right
            # this way our values will be already sorted :)
            dfs(node.left, vals)
            vals.append(node.val)
            dfs(node.right, vals)

            return vals


        vals = dfs(root, [])

        if k - 1 >= len(vals):
            return vals[-1]

        return vals[k - 1]


s = Solution()
root = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(5))
print(s.kthSmallest(root, 4))  # 5
