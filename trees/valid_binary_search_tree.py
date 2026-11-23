from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution__:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # bst means everything on the left is smaller than current val
        # and everything greater is on the right

        # requires specific traversal order, the sequence
        # `left -> node -> right` must be strictly increasing
        prev = None
        def dfs(node):
            if node is None:
                return True

            if not dfs(node.left):
                return False

            nonlocal prev
            if prev is not None and prev >= node.val:
                return False

            prev = node.val
            return dfs(node.right)

        return dfs(root)



class Solution_:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        cur = root
        prev = None

        # more clean approach would be using stack:
        # add elements until we exhaust left, then pop current element, assign `prev`
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if prev is not None and prev >= cur.val:
                return False

            prev = cur.val
            cur = cur.right

        return True


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # my idea was to use different traversal, for this approach we have to carry (low, high) bound
        def dfs(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))


s = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(s.isValidBST(root))  # True
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isValidBST(root))  # False
root = TreeNode(2, TreeNode(2), TreeNode(2))
print(s.isValidBST(root))  # False
root = TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(1.5)),
                TreeNode(3, TreeNode(2.1),
                    TreeNode(4, TreeNode(3.1), TreeNode(5, None, TreeNode(6, TreeNode(2.1))))))
print(s.isValidBST(root))  # False
