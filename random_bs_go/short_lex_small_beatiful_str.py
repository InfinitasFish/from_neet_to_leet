from __future__ import annotations


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        slsbss = []

        count = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] == '1':
                count += 1

            if count == k:
                slsbss.append(s[left:right + 1])
                while True:
                    if s[left] == '1':
                        count -= 1
                        left += 1
                        break

                    left += 1
                    slsbss.append(s[left:right + 1])

            right += 1

        if len(slsbss) == 0:
            return ""

        slsbss = sorted(slsbss, key=len)
        min_len = len(slsbss[0])
        candidates = [c for c in slsbss if len(c) == min_len]
        return min(candidates)


s = Solution()
print(s.shortestBeautifulSubstring("100011001", 3))  # 11001
print(s.shortestBeautifulSubstring("10001100100", 3))
print(s.shortestBeautifulSubstring("000", 1))  # ""
