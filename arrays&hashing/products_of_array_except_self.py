from __future__ import annotations

from itertools import product


class SolutionUnoptimized:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(3n) is doable if we accumulate products in prefix and postfix
        prefix = nums.copy()
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i - 1]

        postfix = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] *= postfix[i + 1]

        # so having prefix and postfix product for each idx, resulting product
        # for 'i' will be prefix[i - 1] * postfix[i + 1], because both won't include nums[i]
        products = [1] * len(nums)
        products[0] = postfix[1]
        products[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            products[i] = prefix[i - 1] * postfix[i + 1]

        return products


class SolutionFaster:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        # little optimization, we can calc pref and postf on the fly
        prefix = nums[0]
        for i in range(1, len(nums)):
            products[i] *= prefix
            prefix *= nums[i]

        postfix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]

        return products


print(SolutionFaster().productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(SolutionFaster().productExceptSelf([1,2,4,6]))  # [48,24,12,8]
print(SolutionFaster().productExceptSelf([-1,0,1,2,3]))  # [0,-6,0,0,0]