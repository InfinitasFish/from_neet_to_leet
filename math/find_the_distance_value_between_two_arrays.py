from __future__ import annotations
from bisect import bisect_left


class Solution_:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # ty for easy daily
        # Ot(n*m)

        res = 0
        for i in range(len(arr1)):
            f = False
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    f = True
                    break

            if not f:
                res += 1

        return res


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # binary search O((n + m)log_m)
        # |a - b| >= d  ->  window [a - d, a + d] not in arr2
        # sort arr2, bisect_left by `a - d` (insertion point),
        # and check whether returned arr2[idx] is larger than `a + d`
        arr2 = sorted(arr2) + [10e5]
        res = 0
        for n in arr1:
            if arr2[bisect_left(arr2, n - d)] > n + d:
                res += 1

        return res


s = Solution()
print(s.findTheDistanceValue([4,5,8], [10,9,1,8], 2))  # 2
print(s.findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3))  # 2
