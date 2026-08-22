from __future__ import annotations
from time import perf_counter


# bro this solution actually beats only 5% submissions by time HAHAHAHAHAA
# I've peaked
class SolutionSlow:
    def canJump(self, nums: List[int]) -> bool:
        # I guess we jump only forward
        def dfs(idx, nums, dp):
            if idx + nums[idx] >= len(nums) - 1:
                return True

            if dp[idx] == False:
                return False

            for i in range(1, nums[idx] + 1):
                next_step = dfs(idx + i, nums, dp)
                if next_step:
                    return True

            dp[idx] = False
            return False

        can_jump = dfs(0, nums, [""] * len(nums))
        return can_jump


class SolutionFast:
    def canJump(self, nums: List[int]) -> bool:
        # okay...
        # basically because we're allowed to move to any number of indexes
        # from 1 up to nums[idx] at idx, we can simplify the solution drastically
        move_steps = nums[0]
        for i in range(1, len(nums)):
            if move_steps <= 0:
                return False

            move_steps -= 1
            if nums[i] > move_steps:
                move_steps = nums[i]

        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP solution that utilizes back-to-front approach:
        # if we can reach index before last, we set this index as last
        # that's the idea
        last = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last:
                last = i

        return True if last == 0 else False


if __name__ == "__main__":
    s = SolutionSlow()
    start = perf_counter()
    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJump([3, 2, 1, 0, 4]))  # False
    print(s.canJump([1]))  # True
    [s.canJump([3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4])
     for i in range(1000000)]
    sl = perf_counter() - start

    s = SolutionFast()
    start = perf_counter()
    print(s.canJump([2,3,1,1,4]))  # True
    print(s.canJump([3,2,1,0,4]))  # False
    print(s.canJump([1]))  # True
    [s.canJump([3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4])
     for i in range(1000000)]
    sf = perf_counter() - start

    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJump([3, 2, 1, 0, 4]))  # False
    print(s.canJump([1]))  # True
    [s.canJump([3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4])
     for i in range(1000000)]
    sd = perf_counter() - start

    print(f"Orig sol time: {sl:.2f}, Fast sol time: {sf:.2f}, Dp sol time: {sd:.2f}")


