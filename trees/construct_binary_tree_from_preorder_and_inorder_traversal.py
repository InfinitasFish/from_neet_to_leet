from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is root -> left -> right
        # inorder is left -> root -> right

        # non-trivial problem
        # inorder list can be used to split left and right parts of the tree
        # we take root from preorder[0], find it in the inorder,
        # and this will be splitting point
        # do this recursively, get the answer

        if len(inorder) == 0:
            return None

        def dfs(preorder, inorder):
            if len(preorder) == 0:
                return

            root = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            root.left = dfs(preorder[1:idx + 1], inorder[:idx])
            root.right = dfs(preorder[idx + 1:], inorder[idx + 1:])
            return root

        # map breaks solution
        # inorder_map = {k: v for v, k in enumerate(inorder)}
        return dfs(preorder, inorder)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # map and pointers instead of slices

        if len(preorder) == 0:
            return

        def dfs(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return

            root = TreeNode(preorder[pre_left])
            mid = inorder_map[preorder[pre_left]]
            left_size = mid - in_left

            root.left = dfs(pre_left + 1, pre_left + left_size, in_left, mid - 1)
            root.right = dfs(pre_left + left_size + 1, pre_right, mid + 1, in_right)

            return root

        inorder_map = {k:v for v, k in enumerate(inorder)}
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)



s = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))
print(s.buildTree([1,2,3,4], [2,1,3,4]))

