from __future__ import annotations


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute-force would be to find all permutations of len(s2) and check for s2
        # better is to do sliding window of len(s2)
        # sum([ord(c) for c in s1]) isn't good solutions because then "bbb" == "abc"
        if len(s1) > len(s2):
            return False

        s1_freqs = {}
        for c in s1:
            s1_freqs[c] = s1_freqs.get(c, 0) + 1

        window_freqs = {}
        for c in s2[:len(s1) - 1]:
            window_freqs[c] = window_freqs.get(c, 0) + 1

        l = 0
        for r in range(len(s1) - 1, len(s2)):
            window_freqs[s2[r]] = window_freqs.get(s2[r], 0) + 1
            if window_freqs == s1_freqs:
                return True

            window_freqs[s2[l]] -= 1
            if window_freqs[s2[l]] == 0:
                del window_freqs[s2[l]]
            l += 1

        return False


s = Solution()
print(s.checkInclusion("abc", "lecabee"))  # True
print(s.checkInclusion("abc", "lecaabee"))  # False

