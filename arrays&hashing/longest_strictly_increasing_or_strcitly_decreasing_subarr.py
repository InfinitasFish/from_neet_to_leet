from __future__ import annotations


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        dec = 1
        inc = 1
        res = 0
        for i in range(1, len(nums)):
            res = max(res, dec, inc)
            if nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            elif nums[i] > nums[i - 1]:
                dec = 1
                inc += 1
            else:
                dec = 1
                inc = 1

        res = max(res, dec, inc)
        return res


s = Solution()
print(s.longestMonotonicSubarray([1,4,3,3,2]))  # 2
print(s.longestMonotonicSubarray([1,1,1,1,1]))  # 1
print(s.longestMonotonicSubarray([3,2,1]))  # 3
