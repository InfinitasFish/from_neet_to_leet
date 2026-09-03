# love these names
from __future__ import annotations


class SolutionSlow:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # we can swap any number of times
        # first of all we sort numbers, then we can group numbers into swappable groups, by checking whether
        # we do it on sorted copy to ensure proper order in each group - from smaller to bigger
        # after that we iterate on original array and check number's group, then append the smallest number within
        # this group in the result
        nums_ = sorted(nums)

        group_idx = 0
        num_to_group = {nums_[0]: group_idx}
        group_to_nums = {group_idx: [nums_[0]]}

        for i in range(1, len(nums_)):
            if nums_[i] - nums_[i - 1] > limit:
                group_idx += 1

            num_to_group[nums_[i]] = group_idx

            if group_idx in group_to_nums:
                group_to_nums[group_idx].append(nums_[i])
            else:
                group_to_nums[group_idx] = [nums_[i]]

        smallest_arr = []
        for i in range(len(nums)):
            smallest_arr.append(group_to_nums[num_to_group[nums[i]]][0])
            # instead of delete we can convert groups to iterator and use next()
            del(group_to_nums[num_to_group[nums[i]]][0])

        return smallest_arr


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # optimized version, sort elements together with their idx and identify groups from sorted order
        arr = sorted([(v, i) for i, v in enumerate(nums)], key=lambda x: x[0])
        i = 0

        while i < len(nums):
            j = i + 1
            while j < len(nums) and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            idx = sorted(x[1] for x in arr[i:j])
            for k in range(len(idx)):
                nums[idx[k]] = arr[i + k][0]

            i = j

        return nums


s = Solution()
print(s.lexicographicallySmallestArray([1,5,3,9,8], 2))  # [1,3,5,8,9]
print(s.lexicographicallySmallestArray([1,7,6,18,2,1], 3))  # [1,6,7,18,1,2]
print(s.lexicographicallySmallestArray([2,1,1,2,1,2,1], 1))  # [1,1,1,1,2,2,2]
