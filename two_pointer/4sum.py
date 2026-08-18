# bro, whym 4sum, is it gonna end at some point?
# hopefully not with 'n_sum'
from __future__ import annotations
from time import perf_counter
from three_sum_closest import BIG


# my orig solution derived from 2sum and 3sum
class SolutionSlow:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # standard tactic, first sort nums, then run 3 sum for each number
        # time O[nlog(n) + n^3] = O(n^3)
        def threeSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            n = len(nums)
            sums_set = set()
            for i in range(n - 2):
                l = i + 1
                r = n - 1
                while l < r:
                    sum = nums[i] + nums[l] + nums[r]
                    if sum == target:
                        triple = tuple([nums[i], nums[l], nums[r]])
                        if triple not in sums_set:
                            sums_set.add(triple)
                            result.append(list(triple))
                        l += 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1

            return result

        nums = sorted(nums)
        result = []
        sums_map = set()
        for i in range(len(nums) - 3):
            target_hat = target - nums[i]
            three_sums = threeSum(nums[i + 1:], target_hat)
            for s in three_sums:
                quadruple = tuple([nums[i], *s])
                if quadruple not in sums_map:
                    sums_map.add(quadruple)
                    result.append(list(quadruple))

        return result


# a bit different solution which could be faster
# the idea is that instead of checking whether new_sum is in map or not, we just jump over equal numbers
# after finding valid quadruple to ensure no duplicates appear
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        quadruples = []
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                t_hat = target - nums[i] - nums[j]
                l = j + 1
                r = n - 1
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == t_hat:
                        quadruples.append([nums[i], nums[j], nums[l], nums[r]])
                        # jump over duplicate values
                        while l + 1 < n and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1

                    elif sum < t_hat:
                        l += 1
                    else:
                        r -= 1

                # jump over duplicate values
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
                j += 1

            # jump over duplicate values
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            i += 1

        return quadruples


if __name__ == "__main__":
    s = SolutionSlow()
    start = perf_counter()
    print(s.fourSum([1,0,-1,0,-2,2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(s.fourSum([2,2,2,2,2], 8))  # [[2,2,2,2]]
    print(s.fourSum(BIG, 2769))
    sl = perf_counter() - start

    s = Solution()
    start = perf_counter()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(s.fourSum([2, 2, 2, 2, 2], 8))  # [[2,2,2,2]]
    print(s.fourSum(BIG, 2769))
    sf = perf_counter() - start

    print(f"My solution time: {sl:.2f}, Alternative solution time: {sf:.2f}")

