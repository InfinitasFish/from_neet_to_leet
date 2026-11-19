from __future__ import annotations


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # [1,4,7,8,5] -> [1,4,5,7,8] -> [8,1] [7,4]
        if len(nums) == 3:
            return 0

        nums = sorted(nums)
        n = len(nums)

        return min(
            nums[n-3] - nums[0], # keep a[0..n-3]
            nums[n-2] - nums[1], # keep a[1..n-2]
            nums[n-1] - nums[2], # keep a[2..n-1]
        )


