from __future__ import annotations
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k_best = float("inf")
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)

            if hours > h:
                left = mid + 1
            elif hours <= h:
                k_best = mid if mid < k_best else k_best
                right = mid - 1

        return k_best


# print(Solution().minEatingSpeed([1, 4, 3, 2], 9))  # 2
# print(Solution().minEatingSpeed([25,10,23,4], 4))  # 25
print(Solution().minEatingSpeed([312884470], 312884469))  # 2
