from __future__ import annotations


class Solution_:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # brute-force, take windows of every size, collect all sub arrays,
        # count odd sums, TLE because of O(n*n*size) ~ O(n^3)
        res = 0
        for size in range(1, len(arr) + 1):
            for i in range(len(arr) - size + 1):
                csum = sum(arr[i:i+size])
                if csum % 2 == 1:
                    res += 1

        return res % (10**9 + 7)


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # sum(arr[i:j]) == sum(arr[:j]) - sum(arr[:i])
        # decide whether `sum(arr[:j]) - sum(arr[:i])` is odd
        # even - even = even, odd - even = odd, odd - odd = even
        # sooo

        prefix = [0]
        csum = 0
        for n in arr:
            csum += n
            prefix.append(csum)

        # ex. prefix [0, 1, 4, 9] -> even 0&4, odd 1&9
        # 0 to 1 is [1], 0 to 9 is [1,3,5], 1 to 4 is [3], 4 to 9 is [5]
        even = sum([1 for n in prefix if n % 2 == 0])
        odd = sum([1 for n in prefix if n % 2 == 1])

        return even * odd % (10**9 + 7)


s = Solution()
print(s.numOfSubarrays([1,3,5]))  # 4
print(s.numOfSubarrays([2,4,6]))  # 0
print(s.numOfSubarrays([1,2,3,4,5,6,7]))  # 16

