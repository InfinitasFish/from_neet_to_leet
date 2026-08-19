from __future__ import annotations


class Solution:
    def trap(self, height: List[int]) -> int:
        # the idea is to keep two pointers and current max_left and max_right
        # let's say our max_left=0 and max_right=1, to find the max possible trapped water
        # we will take smaller max_left, to have a guarantee that water doesn't spill out
        # and calc amount of water max(0, max_left - height[l]) to avoid negative values
        # after that we update left ptr, because we don't need to find new max_right, but we want to find
        # new max_left to maximize possible trapped water (remember we take smaller max to update result)
        l = 0
        r = len(height) - 1
        max_left = 0
        max_right = 0
        result = 0

        while l < r:
            if height[l] > max_left:
                max_left = height[l]
            if height[r] > max_right:
                max_right = height[r]

            if max_right > max_left:
                result += max(0, max_left - height[l])
                l += 1
            else:
                result += max(0, max_right - height[r])
                r -= 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(s.trap([4,2,0,3,2,5]))  # 9
    print(s.trap([0,0,0,1,1,1,2,2,2]))  # 0
    print(s.trap([4,2,3]))  # 1
