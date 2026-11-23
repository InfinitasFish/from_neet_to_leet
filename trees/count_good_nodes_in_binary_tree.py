from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        M = -(10**6)

        # keep max value for each path
        def dfs(node, max_):
            if node is None:
                return

            if node.val >= max_:
                nonlocal res
                res += 1

            max_ = max(max_, node.val)
            dfs(node.left, max_)
            dfs(node.right, max_)

        dfs(root, M)
        return res


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # moving in result variable inside the dfs
        # just because

        M = -(10**6)
        def dfs(node, max_, count):
            if node is None:
                return 0

            if node.val >= max_:
                count += 1
                max_ = node.val

            count += dfs(node.left, max_, 0)
            count += dfs(node.right, max_, 0)

            return count

        return dfs(root, M, 0)


s = Solution()
root = TreeNode(2, TreeNode(1, TreeNode(3)),
                TreeNode(1, TreeNode(1), TreeNode(5)))
print(s.goodNodes(root))  # 3
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(-1))
print(s.goodNodes(root))  # 4
