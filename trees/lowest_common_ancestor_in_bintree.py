from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # original idea, not optimal
        # first of all we find the nodes `p` and `q`, then we collect the list of ancestors to these nodes
        # and last thing is to find first mismatch in these list, element before mismatch is LCA

        def find(p, val):
            if p is None:
                return

            if p.val == val:
                return p

            left = find(p.left, val)
            if left is not None:
                return left

            return find(p.right, val)

        p_node = find(root, p.val)
        q_node = find(root, q.val)

        def dfs(p, val, cur):
            if p is None:
                return []

            if p.val == val:
                return cur + [p.val]

            left = dfs(p.left, val, cur + [p.val])

            if left:
                return left

            return dfs(p.right, val, cur + [p.val])

        ancestors_p = dfs(root, p_node.val, [])
        ancestors_q = dfs(root, q_node.val, [])

        for i in range(min(len(ancestors_p), len(ancestors_q))):
            if ancestors_p[i] != ancestors_q[i]:
                return TreeNode(ancestors_p[i-1])

        if len(ancestors_p) < len(ancestors_q):
            return TreeNode(ancestors_p[-1])
        return TreeNode(ancestors_q[-1])


s = Solution()
root = TreeNode(5, TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)),
                TreeNode(8, TreeNode(7), TreeNode(9)))
print(s.lowestCommonAncestor(root, TreeNode(3), TreeNode(8)))  # 5
print(s.lowestCommonAncestor(root, TreeNode(3), TreeNode(4)))  # 3
