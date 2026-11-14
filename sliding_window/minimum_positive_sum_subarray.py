from __future__ import annotations


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # tried dynamic sliding window, deciding the step by greedy logic, didn't work out,
        # because you can't really define greedy logic that covers all cases
        INF = 10**10
        min_sum = INF
        if len(nums) == 0:
            return -1

        # check for all fixed window's sizes,
        # O(sizes * n) ~ O(n) if (r - l + 1) << n
        for size in range(l, r + 1):
            csum = 0
            for i in range(len(nums)):
                csum += nums[i]
                if i >= size:
                    csum -= nums[i - size]
                if (i >= size - 1) and (0 < csum < min_sum):
                    min_sum = csum

        return min_sum if min_sum != INF else -1


s = Solution()
print(s.minimumSumSubarray([3,-2,1,4], 2, 3))  # 1
print(s.minimumSumSubarray([1,2,3,4], 2, 4))  # 3
print(s.minimumSumSubarray([-6, -6, -6, -6], 2, 3))  # -1
print(s.minimumSumSubarray([4,3,2,1], 1, 1))  # 1
print(s.minimumSumSubarray([20,-7,-12], 2, 3))  # 1
print(s.minimumSumSubarray([-3,17], 1,2))  # 14
