from __future__ import annotations


class SolutionSlow:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # brute-force
        n = len(img1)
        def shift(x, y):
            num = 0
            for row in range(n):
                for col in range(n):
                    if (0 <= col + x < n and 0 <= row + y < n
                        and img1[row + y][col + x] == 1
                        and img2[row][col] == 1):
                        num += 1

            return num

        sums = []
        for x in range(-n, n):
            for y in range(-n, n):
                sums.append(shift(x, y))

        return max(sums)


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a1 = [(x, y) for x in range(n) for y in range(n) if img1[y][x]]
        b1 = [(x, y) for x in range(n) for y in range(n) if img2[y][x]]

        shifts = {}
        for xa, ya in a1:
            for xb, yb in b1:
                # basically 's' is a shift that we need to align two particular 'ones'
                # we count how many of each shift appears, which will give us information about max overlap
                # e.g. if we get (-1, -1) shift three times, it means that shifting image this way will give
                # us an overlap of three 'ones'
                s = (xa - xb, ya - yb)
                shifts[s] = shifts.get(s, 0) + 1

        # we return which shift appears the most
        return max(shifts.values()) if shifts.values() else 0


s = Solution()
print(s.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]))  # 3
