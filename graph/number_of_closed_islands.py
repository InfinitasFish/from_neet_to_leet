from __future__ import annotations


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        count = 0

        def dfs(i, j):
            nonlocal count
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 1:
                return

            grid[i][j] = 1
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        # clear out bordering islands first
        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0]) - 1)

        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid) - 1, j)

        # count remaining islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # guaranteed to be closed
                    count += 1
                    dfs(i, j)

        return count


s = Solution()
print(s.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))  # 2
