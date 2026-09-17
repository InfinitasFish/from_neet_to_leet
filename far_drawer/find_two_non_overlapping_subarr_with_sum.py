from __future__ import annotations


class Solution:
    # I have no clue
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        # two sub arrays with min length, each has sum == target
        n = len(arr)
        res = n + 1
        sum = 0
        i = 0
        # min len of target subarray before 'j'
        dp = [n] * (n + 1)
        for j in range(n):
            sum += arr[j]

            while sum > target:
                sum -= arr[i]
                i += 1

            dp[j + 1] = dp[j]
            if sum == target:
                len = j - i + 1
                res = min(res, len + dp[i])
                dp[j + 1] = min(dp[j], len)

        return -1 if res == n + 1 else res


s = Solution()
print(s.minSumOfLengths([3,2,2,4,3], 3))  # 2
print(s.minSumOfLengths([7,3,4,7], 7))  # 2
print(s.minSumOfLengths([4,3,2,6,2,3,4], 6))  # -1
print(s.minSumOfLengths([1,6,1], 7))  # -1
