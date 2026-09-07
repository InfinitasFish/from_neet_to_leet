from __future__ import annotations


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        stable_index = -1
        for i in range(len(nums)):
            max_before = max(nums[:i + 1])
            min_after = min(nums[i:])
            diff = max_before - min_after
            if diff <= k:
                stable_index = i
                break

        return stable_index


s = Solution()
print(s.firstStableIndex([5,0,1,4], 3))  # 3
print(s.firstStableIndex([4,3], 3))  # 0
