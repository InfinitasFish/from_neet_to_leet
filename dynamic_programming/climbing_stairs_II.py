from __future__ import annotations
from functools import cache


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # i -> i+1, i+2, i+3
        # cost = costs[j] + (j - i)^2
        costs = [0] + costs
        inf = 10 ** 10

        # without cache exceeds time limit
        @cache
        def step(idx):
            # calculates minimum cost to the end from idx
            if idx > n:
                return inf
            if idx == n:
                return costs[n]

            # check each possible step, calculate cost as costs[i] + (cost of next step) + (distance cost)
            return costs[idx] + min(step(idx + 1) + 1, step(idx + 2) + 4, step(idx + 3) + 9)

        return step(0)


s = Solution()
print(s.climbStairs(4, [1,2,3,4]))  # 13

