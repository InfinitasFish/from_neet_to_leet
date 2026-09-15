from __future__ import annotations


class SolutionSlow:
    def maxPalindromes(self, s: str, k: int) -> int:
        # brute force solution would be to find all palindromes of length >= 'k',
        # then find all non-overlapping combinations and return the longest one
        # which is somewhere O(n^3 + n^2)

        # find max number of non-overlapping palindromes of length >= 'k'
        n = len(s)
        # a table that can show whether s[i:i + k] is a palindrome for any 'k'
        # due to dp nature (reusing previous length info to check for palindrome)
        # this will be O(n^2)
        isPalindrome = [[False] * n for _ in range(n)]
        # check all lengths from 1 to n
        for l in range(1, n + 1):
            # limit upper bound to not get out of string's len
            for left in range(n - l + 1):
                right = left + l - 1
                if s[left] == s[right] and (l <= 2 or isPalindrome[left + 1][right - 1]):
                    isPalindrome[left][right] = True

        # dp to keep the current max of non-overlapping substrings
        dp = [0 for i in range(n)]
        for i in range(n):
            if i > 0:
                dp[i] = dp[i - 1]

            for j in range(i - k + 2):
                if isPalindrome[j][i]:
                    # to ensure non-overlapping, we get the previous max using idx before left pointer 'j'
                    prev = dp[j - 1] if j - 1 >= 0 else 0
                    dp[i] = max(dp[i], prev + 1)

        return dp[n - 1]


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        # we can find palindromes by treating each character (for odd length palindromes)
        # or a pair of characters (for even length palindromes) as center, and expand it to left and right
        # to count them we will use greedy principle: find a valid palindrome as early as possible and continue
        # to ensure non-overlapping we will mark last index of found palindrome
        n = len(s)
        res = 0
        end = -1

        for i in range(n):
            for l0 in (i - 1, i):
                # start from center (i, i) or (i - 1, i)
                left, right = l0, i
                while left >= 0 and right < n and s[left] == s[right]:
                    if right - left + 1 >= k and left > end:
                        res += 1
                        end = right
                        break

                    left -= 1
                    right += 1

        return res


s = Solution()
print(s.maxPalindromes("abaccdbbd", 3))  # 2
print(s.maxPalindromes("adbcda", 2))  # 0
print(s.maxPalindromes("ababa", 3))  # 1
