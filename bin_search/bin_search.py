from __future__ import annotations


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        if nums[len(nums) - 1] == target:
            return len(nums) - 1

        left = 1
        right = len(nums) - 1

        min_idx = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[min_idx]:
                min_idx = mid
                right = mid - 1
            elif nums[mid] > nums[min_idx]:
                left = mid + 1

        left = 0
        right = len(nums) - 1
        if min_idx > left and target >= nums[left]:
            right = min_idx
        else:
            left = min_idx

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

print(Solution().search([3,4,5,6,1,2], 1))  # 4
print(Solution().search([-1,0,2,4,6,8], 4))  # 3
print(Solution().search([3,1], 3))  # 0
