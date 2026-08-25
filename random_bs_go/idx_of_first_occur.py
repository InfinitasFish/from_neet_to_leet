from __future__ import annotations


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = -1
        left = 0
        while left < len(haystack):
            if haystack[left] == needle[0] and left + len(needle) - 1 < len(haystack):
                sub = haystack[left:left + len(needle)]
                if sub == needle:
                    idx = left
                    break

            left += 1

        return idx


s = Solution()
print(s.strStr("mississippi", "issip"))
print(s.strStr("a", "a"))
print(s.strStr("aa", "aaa"))
