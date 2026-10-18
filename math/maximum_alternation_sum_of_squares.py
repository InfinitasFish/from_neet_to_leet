from __future__ import annotations


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...
        # big numbers on odd, small on even
        # because we take squares, we sort nums by absolute value

        n = len(nums)
        nums = sorted(nums, key=lambda x: abs(x), reverse=True)
        score = 0

        for i in range(n // 2):
            score += nums[i] * nums[i]
            score -= nums[-(i + 1)] * nums[-(i + 1)]

        if n % 2 == 1:
            score += nums[n // 2] * nums[n // 2]

        return score


s = Solution()
print(s.maxAlternatingSum([1,2,3]))  # 12
