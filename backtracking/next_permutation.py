from __future__ import annotations


class Solution_:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # brute-force, TLE
        def perms(lst):
            if len(lst) <= 1:
                return [lst[:]]

            result = []
            for i, item in enumerate(lst):
                rest = lst[:i] + lst[i+1:]
                for p in perms(rest):
                    result.append([item] + p)

            return result

        permutations = sorted(perms(nums))
        idx = idx_ = permutations.index(nums)

        # skip duplicate permutations
        while idx < len(permutations) - 1 and permutations[idx] == permutations[idx + 1]:
            idx += 1

        if idx + 1 == len(permutations) and permutations[idx_]:
            t = permutations[0]
        else:
            t = permutations[idx + 1]

        for i, n in enumerate(t):
            nums[i] = n

        return


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # idea - move the minimally higher element up
        # which and where though?
        # we need to find decreasing element from the right
        # and swap it with minimal bigger element

        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = reversed(nums[i:])
        return


s = Solution()
print(s.nextPermutation([1,5,1]))
print(s.nextPermutation([1,3,2]))
