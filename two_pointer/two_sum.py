from __future__ import annotations


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]


print(Solution().twoSum([1, 1, 2, 4, 5, 6, 7], 10))  # 4, 6
print(Solution().twoSum([-5, 1, 2, 4, 5, 6, 7], 2))  # 1, 7
print(Solution().twoSum([-5, 1, 2, 4, 5, 6, 7], 2))  # 1, 7
