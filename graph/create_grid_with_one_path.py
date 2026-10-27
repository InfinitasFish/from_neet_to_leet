from __future__ import annotations


class Solution_:
    def createGrid(self, m: int, n: int) -> list[str]:
        # clever bad
        path = [["#"] * n for _ in range(m)]

        idx = 0
        while idx < m - 1 and idx < n - 1:
            path[idx][idx] = "."
            path[idx][idx + 1] = "."
            idx += 1

        if idx == m - 1:
            while idx < n:
                path[m - 1][idx] = "."
                idx += 1
        elif idx == n - 1:
            while idx < m:
                path[idx][n - 1] = "."
                idx += 1

        return [''.join(p) for p in path]


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # simple good
        path = []
        for i in range(m):
            if i == 0:
                path.append("." * n)
            else:
                path.append()

        return path


s = Solution()
print(s.createGrid(2, 3))  # ["..#","#.."]
print(s.createGrid(3, 3))
print(s.createGrid(1, 4))
print(s.createGrid(4, 1))
