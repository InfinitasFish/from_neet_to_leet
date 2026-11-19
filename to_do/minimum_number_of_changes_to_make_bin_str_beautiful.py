from __future__ import annotations


class Solution:
    def minChanges(self, s: str) -> int:
        if len(s) % 2 == 1:
            return -1

        for size in range(2, len(s) // 2, 2):
            return

s = Solution()
print(s.minChanges("1001"))  # 2
