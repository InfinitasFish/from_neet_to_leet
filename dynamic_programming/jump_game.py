from __future__ import annotations


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


if __name__ == "__main__":
    s = SolutionSlow()
    print(s.canJump([2,3,1,1,4]))  # True
    print(s.canJump([3,2,1,0,4]))  # False
    print(s.canJump([1]))  # True


