from __future__ import annotations


# cool
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        max_area = 0
        for i in range(1, len(heights)):
            popped_idx = i
            while stack and heights[i] < stack[-1][1]:
                start_idx, height = stack.pop()
                popped_idx = start_idx
                area = (i - start_idx) * height
                if area > max_area:
                    max_area = area

            stack.append((popped_idx, heights[i]))

        while stack:
            start_idx, height = stack.pop()
            area = (len(heights) - start_idx) * height
            if area > max_area:
                max_area = area

        return max_area


ts = [
      ([2,3,4,3], 9),
      ([7,1,7,2,2,4], 8),
      ([1,3,7], 7),
      ([2,1,5,6,2,3], 10),
      ([3,6,5,7,4,8,1,0], 20)
      ]
s = Solution()
for (heights, target) in ts:
    print(f"{str(heights):<30} : {s.largestRectangleArea(heights):<3} ({target})")