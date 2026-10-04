from __future__ import annotations


class SolutionSlow:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        freqs = [0] * 26
        l = 0
        r = 1
        freqs[ord(s[0]) - 65] += 1
        freqs[ord(s[1]) - 65] += 1
        max_seq = 0
        while l < len(s):
            to_replace = sum(freqs) - max(freqs)
            if to_replace > k:
                freqs[ord(s[l]) - 65] -= 1
                l += 1
                continue

            if r - l + 1 > max_seq:
                max_seq = r - l + 1
            if r + 1 < len(s):
                r += 1
                freqs[ord(s[r]) - 65] += 1
            else:
                freqs[ord(s[l]) - 65] -= 1
                l += 1

        return max_seq


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_freq = 0
        # faster because of 'for' cycle and
        # (r - l + 1 - max_freq) instead of (sum(freqs) - max(freqs))
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            max_freq = max(max_freq, count[s[r]])
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


s = Solution()
print(s.characterReplacement("XYYX", 2))  # 4
print(s.characterReplacement("AAABABB", 1))  # 5
