from __future__ import annotations
from math import floor


# we can do better
class SolutionBigRange:
    def countCommas(self, n: int) -> int:
        # total number of commas used to write all integers from [1, n]
        if n < 1000:
            return 0

        step = 1
        while 1000 ** (step + 1) <= n:
            step += 1

        count = 0
        while step > 0:
            commas = (n - 1000 ** step) * step + 1
            count += commas
            n = n - commas // step
            step -= 1

        return count


# so-called better
class Solution:
    def countCommas(self, n: int) -> int:
        # basically we can just iterate from 1000 to n and increment counter by 1
        # it works only because we are constrained by 1 <= n <= 10^5
        # so we don't have to worry about numbers with two commas...
        return max(0, n - 999)


s = SolutionBigRange()
print(s.countCommas(1024))  # 25
print(s.countCommas(2019))  # 1020
print(s.countCommas(1000))  # 1
print(s.countCommas(998))  # 0
s = SolutionBigRange()
print(s.countCommas(1000000))  # 999002

