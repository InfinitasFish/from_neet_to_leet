from __future__ import annotations


class SolutionSlow:
    def maxSubArray(self, nums: List[int]) -> int:
        # my idea is to keep two pointers, with and check whether
        # nums[left] + nums[left + 1] > nums[right] + nums[right - 1]
        # and move pointer with smaller sum, but we'd have to calculate sum
        # on each step, which is O(n)

        # upd. idea doesn't work because [left + 1] window is not always sufficient
        # to find the optimal move, e.g. on [0,0,-3,1]
        # next idea is sliding window, though it's O(n^2) time
        left = 0
        max_sum = -float("inf")
        n = len(nums)
        while left < n:
            right = left
            while right < n:
                max_sum = max(max_sum, sum(nums[left:right + 1]))
                right += 1

            left += 1

        return max_sum


class SolutionKadane:
    def maxSubArray(self, nums: List[int]) -> int:
        # better solution is to make a one-pass on nums, on each step we
        # check whether current sum is negative before adding nums[i], if it is,
        # sum resets to 0 before adding nums[i], this way we ensure that we exhaust
        # possible good subarray before finding next candidate

        total = 0
        max_sum = -float("inf")
        for i in range(len(nums)):
            if total < 0:
                total = 0
            total += nums[i]
            max_sum = max(max_sum, total)

        return max_sum


class SolutionDivide:
    def maxSubArray(self, nums: List[int]) -> int:
        # follow-up question to solve it with divide & conquer
        # the idea is that solution can lie in either left part, right part,
        # or part that contains middle index, some part of left and some part of right
        # O(T) = 2*O[nlog(n)] + O(n) = O[nlog(n)]
        def maxSubArray(arr, left, right):
            if left > right:
                return -float("inf")

            mid = left + (right - left) // 2
            left_sum = 0
            right_sum = 0
            cur_sum = 0

            for i in range(mid-1, left-1, -1):
                cur_sum += nums[i]
                left_sum = max(left_sum, cur_sum)

            cur_sum = 0
            for i in range(mid+1, right+1):
                cur_sum += nums[i]
                right_sum = max(right_sum, cur_sum)

            cur_max_sum = left_sum + nums[mid] + right_sum
            next_left_sum = maxSubArray(nums, left, mid-1)
            next_right_sum = maxSubArray(nums, mid+1, right)
            return max(next_left_sum, next_right_sum, cur_max_sum)

        return maxSubArray(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    s = SolutionDivide()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(s.maxSubArray([-1,-2]))  # -1
    print(s.maxSubArray([0,0,-3,1]))  # 1
    print(s.maxSubArray([-1,0,-2]))  # 0
    print(s.maxSubArray([-1,1,2,1]))  # 4
    
    
