from __future__ import annotations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # didn't get it myself, the logic is very clear - at each step we have two branches,
        # to include or not to include a number, after which we will call function recursively
        # the main trick to accomplish that is to pop() last element of current subset before second
        # recursive call, while keeping the step (idx) of iteration
        res = []
        subset = []
        def subsets_(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            subsets_(i + 1)

            subset.pop()
            subsets_(i + 1)

        subsets_(0)
        return res


s = Solution()
print(s.subsets([1,2,3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(s.subsets([7]))  # [[], [7]]
