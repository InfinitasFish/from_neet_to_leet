from __future__ import annotations


# O(4n) -> O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        total_trap = 0
        max_left_i = []
        max_left = 0
        for i in range(len(height)):
            max_left_i.append(max_left)
            if height[i] > max_left:
                max_left = height[i]

        max_right_i = []
        max_right = 0
        for i in range(len(height)-1, -1, -1):
            max_right_i.append(max_right)
            if height[i] > max_right:
                max_right = height[i]

        max_right_i.reverse()

        for i in range(len(height)):
            total_trap += max(0, min(max_left_i[i], max_right_i[i]) - height[i])

        return total_trap


# O(n)
class SolutionFaster:
    def trap(self, height: List[int]) -> int:
        total_trap = 0
        left = 0
        max_left = 0
        right = len(height) - 1
        max_right = 0

        while left < right:
            if height[left] > max_left:
                max_left = height[left]
            if height[right] > max_right:
                max_right = height[right]

            if max_left < max_right:
                total_trap += max(0, max_left - height[left])
                left += 1
            else:
                total_trap += max(0, max_right - height[right])
                right -= 1

        return total_trap


ts = [{"height": [0,2,0,3,1,0,1,3,2,1], "exp": 9},
      {"height": [5,5,5,5,5,1,0,1], "exp": 1},
      {"height": [0,1,0,2,1,0,1,3,2,1,2,1], "exp": 6},
      {"height": [4,2,3], "exp": 1},
      {"height": [5,4,1,2], "exp": 1},
      {"height": [9,6,8,8,5,6,3], "exp": 3},
      {"height": [4,2,0,3,2,5], "exp": 9},]

s = SolutionFaster()
for t in ts:
    print(f"{str(t['height']):<40} : {s.trap(t['height']):<2} ({t['exp']})")

