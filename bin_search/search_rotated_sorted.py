from __future__ import annotations


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        min_idx = 0
        while left <= right:
            if nums[left] < nums[right]:
                min_idx = left if nums[left] < nums[min_idx] else min_idx
                break

            mid = (left + right) // 2
            min_idx = mid if nums[mid] < nums[min_idx] else min_idx
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1
        if nums[min_idx] <= target <= nums[right]:
            left = min_idx
        else:
            right = min_idx - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1
#
# print(Solution().search([3,4,5,6,1,2], 1))  # 4
# print(Solution().search([3,5,6,0,1,2], 4))  # -1
# print(Solution().search([1,3], 3))  # 1
# print(Solution().search([5,1,2,3,4], 1))  # 1
print(Solution().search([4,5,6,7,0,1,2], 0))  # 4
