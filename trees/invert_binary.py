from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # easy problem, swap left and right recursively

        def swap(leaf):
            if leaf is None:
                return

            if leaf.right is not None and leaf.left is not None:
                t = leaf.right
                leaf.right = leaf.left
                leaf.left = t
                swap(leaf.right)
                swap(leaf.left)

            elif leaf.right is not None:
                leaf.left = leaf.right
                leaf.right = None
                swap(leaf.left)

            elif leaf.left is not None:
                leaf.right = leaf.left
                leaf.left = None
                swap(leaf.right)

        swap(root)
        return root


s = Solution()
t = TreeNode(3, TreeNode(2), TreeNode(1))
print(s.invertTree(t))  # [3, 2, 1]
t = TreeNode(1, TreeNode(2))
print(s.invertTree(t))  # [1,None,2]
