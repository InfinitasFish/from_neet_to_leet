from __future__ import annotations


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_freqs = {}
        for c in t:
            t_freqs[c] = t_freqs.get(c, 0) + 1

        l = 0
        min_string = ""
        # the main trick is to use t_count as indicator that shows how many characters we found
        # e.g. if we have t="GGD", we increment t_count after finding two "G" or one "D"
        t_count = 0
        window_freqs = {}
        for r in range(len(s)):
            window_freqs[s[r]] = window_freqs.get(s[r], 0) + 1
            if 0 < t_freqs.get(s[r], 0) == window_freqs.get(s[r], 0):
                t_count += 1

            while t_count == len(t_freqs):
                if not min_string or r - l + 1 < len(min_string):
                    min_string = s[l:r + 1]

                window_freqs[s[l]] -= 1
                if t_freqs.get(s[l], 0) > 0 and window_freqs[s[l]] < t_freqs[s[l]]:
                    t_count -= 1

                l += 1

        return min_string


s = Solution()
print(s.minWindow("OUZODYXAZV", "XYZ"))  # "YXAZ"
print(s.minWindow("ACCBXXXXBA", "AB"))  # "BA"
print(s.minWindow("AB", "A"))  # A
