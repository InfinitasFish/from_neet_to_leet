from __future__ import annotations


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_cur = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                min_cur = min(min_cur, nums[left])
                break

            mid = (left + right) // 2
            min_cur = min(min_cur, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return min_cur


print(Solution().findMin([4,5,0,1,2,3]))
print(Solution().findMin([3,4,5,6,1,2]))
print(Solution().findMin([4,5,6,7]))
print(Solution().findMin([2,1]))
print(Solution().findMin([5,1,2,3,4]))
