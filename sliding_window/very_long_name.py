# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
from __future__ import annotations


class SolutionSlow:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = k - 1
        more_equal_thresh_count = 0
        while right < len(arr):
            # O(sum) scales with k so it's very slow for big k (bottleneck)
            if sum(arr[left:right + 1]) / k >= threshold:
                more_equal_thresh_count += 1
            left += 1
            right += 1

        return more_equal_thresh_count


class SolutionHuman:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # keep current sum instead of doing sum() on each step
        left = 0
        right = k - 1
        cur_sum = sum(arr[left:right])
        more_equal_thresh_count = 0
        while right < len(arr):
            cur_sum += arr[right]
            if cur_sum / k >= threshold:
                more_equal_thresh_count += 1
            cur_sum -= arr[left]
            left += 1
            right += 1

        return more_equal_thresh_count


print(SolutionHuman().numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))  # 3
print(SolutionHuman().numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))  # 6
