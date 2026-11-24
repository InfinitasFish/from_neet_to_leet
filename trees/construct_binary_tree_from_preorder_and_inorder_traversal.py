from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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

            if len(preorder) == 1:
                return TreeNode(preorder[0])

            root = TreeNode(preorder[0])
            # index also tells us how many nodes we take for the left subtree
            idx = inorder.index(preorder[0])
            # create left subtree
            root.left = dfs(preorder[1:idx+1], inorder[:idx])
            # and right subtree
            root.right = dfs(preorder[idx+1:], inorder[idx+1:])

            return root

        return dfs(preorder, inorder)


s = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))
print(s.buildTree([1,2,3,4], [2,1,3,4]))

