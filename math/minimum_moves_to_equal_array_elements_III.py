from __future__ import annotations


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # O(2n)
        res = 0
        max_ = max(nums)

        for n in nums:
            res += max_ - n

        return res


s = Solution()
print(s.minMoves([2,1,3]))  # 3
print(s.minMoves([4,4,5]))  # 2
