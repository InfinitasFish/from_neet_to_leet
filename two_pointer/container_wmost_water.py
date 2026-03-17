from __future__ import annotations


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = -1

        while left < right:
            cur_max = min(heights[left], heights[right]) * (right - left)
            max_area = cur_max if cur_max > max_area else max_area

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area


ts = {
    "easy": [1,7,2,5,4,7,3,6],
    "edge": [2,2,2],
    "hard": [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
}

s = Solution()
for name, case in ts.items():
    print(f'{name}: {s.maxArea(case)}')