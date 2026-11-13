from __future__ import annotations
from collections import deque


class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        starts = deque()  # where each plateau starts, left to right
        ans, water, r = 0, 0, len(nums) - 1
        for l in reversed(range(len(nums))):
            x = nums[l]
            while starts and nums[starts[0]] <= x:  # x floods the plateau that starts at starts[0]
                s = starts.popleft()
                end = starts[0] if starts else r + 1
                water += (x - nums[s]) * (end - s)
            starts.appendleft(l)
            while water > k:  # the right end leaves with its water
                water -= nums[starts[-1]] - nums[r]
                if starts[-1] == r:
                    starts.pop()
                r -= 1
            ans += r - l + 1
        return ans



s = Solution()
#print(s.countNonDecreasingSubarrays([6,3,1,2,4,4], 7))  # 17
#print(s.countNonDecreasingSubarrays([6,3,1,3,6], 4))  # 12
print(s.countNonDecreasingSubarrays([6,5,4,3,2,1], 15))  # 21
print(s.countNonDecreasingSubarrays([6,3,1,2,4,4, -6], 7))  # 18
