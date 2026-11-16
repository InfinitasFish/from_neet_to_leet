from __future__ import annotations


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # easy question
        # O(n*log_n)
        while len(s) > k:
            groups = []
            for i in range(0, len(s), k):
                group = sum([int(n) for n in s[i:i+k]])
                groups.append(str(group))

            s = "".join(groups)

        return s


s = Solution()
print(s.digitSum("11111222223", 3))  # "135
