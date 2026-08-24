from __future__ import annotations


class Solution:
    def jump(self, nums: List[int]) -> int:
        # the same thing as previous problem, but now we need to count
        # minimum number of jumps to reach last index (reach is guaranteed)
        # to jump optimally we need to check all possible jumps [1, nums[idx]]
        # and take one that lead to farther index with a condition that nums[idx] != 0
        # because if we land on 0 we won't be able to jump,
        # though solution passes even without this check
        if len(nums) == 1:
            return 0

        idx = 0
        jump_count = 0
        n = len(nums)
        while idx < n - 1:
            if idx + nums[idx] >= n - 1:
                jump_count += 1
                break

            steps = idx + nums[idx] + 1
            far = -1
            far_idx = -1
            for step in range(idx + 1, steps):
                if step + nums[step] >= far and nums[step] != 0:
                    far = step + nums[step]
                    far_idx = step

            idx = far_idx
            jump_count += 1

        return jump_count


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,1]))  # 1
    print(s.jump([2,3,1,1,4]))  # 2
    print(s.jump([2,3,0,1,4]))  # 2
    print(s.jump([1,1,1,4,0,0,0,1]))  # 4
    print(s.jump([10,9,8,7,6,5,4,3,2,1,1,0]))  # 2
    print(s.jump([5,1,1,2,2,0,]))
