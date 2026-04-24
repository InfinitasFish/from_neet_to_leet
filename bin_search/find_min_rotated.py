from __future__ import annotations


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        min_cur = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= min_cur:
                min_cur = nums[mid]
                right = mid - 1
            elif nums[mid] > min_cur:
                left = mid + 1

        return min_cur

#
# print(Solution().findMin([4,5,0,1,2,3]))
# print(Solution().findMin([3,4,5,6,1,2]))
# print(Solution().findMin([4,5,6,7]))
print(Solution().findMin([2,1]))
