from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def step(p, q):
            if p is None and q is not None:
                return False

            if p is not None and q is None:
                return False

            if p is None and q is None:
                return True

            if p.val != q.val:
                return False

            return step(p.left, q.left) and step(p.right, q.right)

        return step(p, q)


s = Solution()
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isSameTree(p, q))  # True
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(3), TreeNode(2))
print(s.isSameTree(p, q))  # False

