from __future__ import annotations


class SolutionSlow:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        nums_set = set(nums)
        cur_len = 1
        for num in nums_set:
            n = 1
            while num - n in nums_set:
                cur_len += 1
                n += 1
            if cur_len > longest:
                longest = cur_len
            cur_len = 1

        return longest


class SolutionHuman:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the start of sequence then iterate through it
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            # start of the seq
            if num - 1 not in nums_set:
                cur_len = 1
                while num + cur_len in nums_set:
                    cur_len += 1
                if cur_len > longest:
                    longest = cur_len

        return longest


print(SolutionHuman().longestConsecutive([1,2,3,4,7,8]))  # 4
print(SolutionHuman().longestConsecutive([2,2,2,2,2,2,2,2]))  # 1
print(SolutionHuman().longestConsecutive([0,3,2,5,4,6,1,1]))  # 7
print(SolutionHuman().longestConsecutive([2,20,4,10,3,4,5]))  # 4
print(SolutionHuman().longestConsecutive([100,4,200,1,3,2]))  # 4