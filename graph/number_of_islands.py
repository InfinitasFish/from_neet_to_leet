from __future__ import annotations
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            # my little hack to not use 'visited' set
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count


# neet solution using breath-search and deque, iterative not recursive
class Solution_:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()

        def bfs(i, j):
            # to implement breath-first search, we need a data-structure
            q = deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                # we can transform bfs into dfs by simply using .pop() instead of .popleft()
                row, col = q.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = row + dr, col + dc
                    if ((r, c) not in visited and
                        0 <= r < rows and
                        0 <= c < cols and
                        grid[r][c] == '1'):
                        q.append((r, c))
                        visited.add((r, c))

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
                else:
                    visited.add((i, j))

        return count


s = Solution()
print(s.numIslands([
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]))  # 1
print(s.numIslands([
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]))  # 4
