from __future__ import annotations


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # not sure whether there's a solution without collecting all the combinations
        # combination can have repeating numbers and any length

        res = []
        def dfs(idx, set, sum):
            if sum == target:
                res.append(set.copy())
                return
            if idx >= len(nums) or sum > target:
                return

            set.append(nums[idx])
            dfs(idx, set, sum + nums[idx])
            set.pop()
            dfs(idx + 1, set, sum)

        dfs(0, [], 0)
        return res


s = Solution()
print(s.combinationSum([2,5,6,9], 9))

