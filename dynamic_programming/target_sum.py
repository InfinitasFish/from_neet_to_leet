from __future__ import annotations


class Solution_:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        count = 0
        # try every variant, time limit exceeded with O(2^n)
        def step(idx=0, sum=0):
            if idx >= len(nums):
                if sum == target:
                    nonlocal count
                    count += 1
                return

            step(idx + 1, sum - nums[idx])
            step(idx + 1, sum + nums[idx])

        step()
        return count


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # caching speeds things up

        dp = {}
        def step(idx=0, sum=0):
            if idx >= len(nums):
                return 1 if sum == target else 0

            if (idx, sum) in dp:
                return dp[(idx, sum)]

            dp[(idx, sum)] = (
                step(idx + 1, sum + nums[idx]) +
                step(idx + 1, sum - nums[idx])
                     )

            return dp[(idx, sum)]

        step()
        return dp[(0,0)]


s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))  # 5