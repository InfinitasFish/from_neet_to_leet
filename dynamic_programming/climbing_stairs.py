from __future__ import annotations
from math import comb


class Solution_:
    def climbStairs(self, n: int) -> int:
        # education purposes, O(2^n), time limit exceeds
        count = 0

        def step(sum=0):
            if sum > n:
                return
            if sum == n:
                nonlocal count
                count += 1
                return

            step(sum + 1)
            step(sum + 2)

        step()
        return count


class Solution:
    def climbStairs(self, n: int) -> int:
        # if we write down possible combinations,
        # we can see the use of binomial coefficient
        count = 1  # because of [1]*n combination
        for i in range(1, n // 2 + 1):
            # `i` is amount of '2'
            # `(n - 2 * i)` is amount of `1`
            places = i + (n - 2 * i)
            ways = comb(places, i)
            count += ways

        return count


s = Solution()
print(s.climbStairs(2))  # 2
print(s.climbStairs(3))  # 3
print(s.climbStairs(4))  # 5
print(s.climbStairs(20))  # 10946
