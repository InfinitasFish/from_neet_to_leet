from __future__ import annotations


class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (ord(s[i]) - 71 - 2 * (ord(s[i]) - 97)) * (i + 1)

        return res


s = Solution()
print(s.reverseDegree("abc"))  # 148
