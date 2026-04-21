from __future__ import annotations


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                idx = mid
                break

        return idx

print(Solution().search([-1,0,2,4,6,8], 4))
