from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(leaf, count):
            if leaf is None:
                return count

            count += 1
            if leaf.left is not None:
                left_depth = findDepth(leaf.left, count)
            else:
                left_depth = count

            if leaf.right is not None:
                right_depth = findDepth(leaf.right, count)
            else:
                right_depth = count

            return max(left_depth, right_depth)

        depth = findDepth(root, 0)
        return depth


s = Solution()
t = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
print(s.maxDepth(t))  # 3

