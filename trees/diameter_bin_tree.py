from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionSlow:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is length of the longest path between any two nodes
        # my idea is to treat each node as a local root, and calculate diameter as sum of left_depth and left_depth
        cache = {}
        def findDepth(leaf, count):
            if leaf is None:
                return count
            if leaf in cache:
                return cache[leaf]

            count += 1
            cache[leaf] = count
            if leaf.left is not None:
                left_depth = findDepth(leaf.left, count)
            else:
                left_depth = count

            if leaf.right is not None:
                right_depth = findDepth(leaf.right, count)
            else:
                right_depth = count

            max_depth = max(left_depth, right_depth)
            return max_depth

        def findDiameter(leaf, max_dm):
            if leaf is None:
                return max_dm

            dm = findDepth(leaf.left, 0) + findDepth(leaf.right, 0)
            if leaf.left is not None:
                left_dm = findDiameter(leaf.left, dm)
            else:
                left_dm = max_dm
            if leaf.right is not None:
                right_dm = findDiameter(leaf.right, dm)
            else:
                right_dm = max_dm

            return max(dm, left_dm, right_dm)

        diameter = findDiameter(root, 0)
        return diameter


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs(leaf):
            if leaf is None:
                return 0

            l = dfs(leaf.left)
            r = dfs(leaf.right)

            nonlocal res
            res = max(res, l + r)

            return 1 + max(l, r)

        dfs(root)
        return res


s = Solution()
t = TreeNode(1, None, TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4)))
print(s.diameterOfBinaryTree(t))  # 3
t = TreeNode(1, None, TreeNode(3, TreeNode(4, None, TreeNode(6)), TreeNode(5, None, TreeNode(7))))
print(s.diameterOfBinaryTree(t))  # 4

