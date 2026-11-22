from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        abs_level = 0

        # select most-right element for each level
        def dfs(node, cur_level):
            if node is None:
                return

            nonlocal abs_level
            if cur_level == abs_level:
                res.append(node.val)
                abs_level += 1

            dfs(node.right, cur_level+1)
            dfs(node.left, cur_level+1)

        dfs(root, 0)
        return res


s = Solution()
root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
print(s.rightSideView(root))  # [1,3,5]

