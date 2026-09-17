from __future__ import annotations


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # not sure whether there's a solution without collecting all the combinations

        subsets = []
        s = []
        def getCombs(idx):
            if idx >= len(nums):
                subsets.append(s.copy())
                return

            s.append(nums[idx])
            getCombs(idx + 1)

            s.pop()
            getCombs(idx + 1)




s = Solution()
print(s.combinationSum([2,5,6,9], 9))

