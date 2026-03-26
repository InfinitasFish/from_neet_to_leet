from __future__ import annotations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # iterate through every num + find remainder with 2sum -> 3sum
        zero_triplets = []

        for i in range(len(nums)):
            # avoid duplicates to not create same triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            sum_to_find = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] < sum_to_find:
                    left += 1
                elif nums[left] + nums[right] > sum_to_find:
                    right -= 1
                else:
                    zero_triplets.append([nums[i], nums[left], nums[right]])
                    # skipping duplicates to not create same triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1

        return zero_triplets


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(Solution().threeSum([0, 1, 1]))  # []
print(Solution().threeSum([0, 0, 0]))  # [[0, 0, 0]]