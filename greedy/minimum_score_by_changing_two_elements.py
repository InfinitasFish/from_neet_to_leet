from __future__ import annotations


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # [1,4,7,8,5] -> [1,4,5,7,8] -> [8,1] [7,4]
        if len(nums) == 3:
            return 0

        # sort so we can calc max diff easily
        nums = sorted(nums)
        n = len(nums)

        # we can turn two numbers into same `k`, so minimum score
        # will be zero, and we only need to minimize highest difference
        # if we remove two elements (which will be the same after first op),
        # we will have these viable combinations:
        return min(
            nums[n-3] - nums[0], # keep a[0..n-3]
            nums[n-2] - nums[1], # keep a[1..n-2]
            nums[n-1] - nums[2], # keep a[2..n-1]
        )


s = Solution()
print(s.minimizeSum([1,2,3]))  # 0
print(s.minimizeSum([1,4,5,8,9]))  # 
