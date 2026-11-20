from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # number of nodes in both trees is [1, 1000]
        # if root is None and subRoot is None:
        #     return True
        # if root is not None and subRoot is None:
        #     return False
        # if root is None and subRoot is not None:
        #     return False

        vals = []
        def find(p, val):
            if p is None:
                return

            if p.val == val:
                vals.append(p)

            find(p.left, subRoot.val)
            find(p.right, subRoot.val)

        find(root, subRoot.val)

        def step(p, q):
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False

            if p.val != q.val:
                return False

            return step(p.left, q.left) and step(p.right, q.right)

        for q in vals:
            if step(subRoot, q):
                return True

        return False


s = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
subroot = TreeNode(2, TreeNode(4), TreeNode(5))
print(s.isSubtree(root, subroot))  # True


