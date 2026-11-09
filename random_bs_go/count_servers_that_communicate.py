from __future__ import annotations


class Solution_:
    def countServers(self, grid: list[list[int]]) -> int:
        # original but kinda slow due to using hashmap
        # O(nm) time, O(n*m) space
        conn = {}
        res = 0

        # if row have more than 1 computer -> add to result
        # to not over count, add each computer to hashmap
        for i in range(len(grid)):
            row = sum(grid[i][:])
            if row > 1:
                res += row
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        conn[(i, j)] = 1


        for j in range(len(grid[0])):
            col = sum([grid[i][j] for i in range(len(grid))])
            if col > 1:
                res += col
                # eliminate computers that we've already counted in rows
                for i in range(len(grid)):
                    if (i, j) in conn:
                        res -= 1

        return res


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # count once, then look up
        # O(nm) time, O(n+m) space
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]

        res = 0
        for i, row in enumerate(grid):
            for j, server in enumerate(row):
                if server and rows[i] + cols[j] > 2:
                    res += 1

        return res


s = Solution()
print(s.countServers([[1,0], [0,1]]))  # 0
print(s.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))  # 4
print(s.countServers([[1,1,1,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,0,0,0,1],[0,1,0,0,0]]))  # 6
