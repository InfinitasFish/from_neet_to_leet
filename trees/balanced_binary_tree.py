from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# two solutions - naive up-to-bottom and optimized bottom-up
class SolutionSlow:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(leaf, height):
            if leaf is None:
                return height

            left_h, right_h = height, height
            if leaf.left is not None:
                left_h = dfs(leaf.left, height + 1)
            if leaf.right is not None:
                right_h = dfs(leaf.right, height + 1)

            return max(left_h, right_h, height)


        def getDiff(leaf, diff):
            if leaf is None:
                return diff

            ld = diff
            if leaf.left is not None and leaf.right is not None:
                ld = abs(dfs(leaf.left, 1) - dfs(leaf.right, 1))
            elif leaf.left is not None:
                ld = dfs(leaf.left, 1)
            elif leaf.right is not None:
                ld = dfs(leaf.right, 1)

            left_d = getDiff(leaf.left, diff)
            right_d = getDiff(leaf.right, diff)
            return max(ld, left_d, right_d, diff)

        max_diff = getDiff(root, 0)
        return max_diff <= 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(leaf):
            if leaf is None:
                return True, 0

            # exhaust full depth
            left, right = dfs(leaf.left), dfs(leaf.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # increment height from bottom-up
            max_height = 1 + max(left[1], right[1])

            return balanced, max_height

        return dfs(root)[0]


s = Solution()
t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#print(s.isBalanced(t))  # True
t = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
#print(s.isBalanced(t))  # False
t = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
#print(s.isBalanced(t))  # False
t = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
print(s.isBalanced(t))  # False

