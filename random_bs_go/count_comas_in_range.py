from __future__ import annotations
from math import floor


# we can do better
class SolutionDirty:
    def countCommas(self, n: int) -> int:
        # total number of commas used to write all integers from [1, n]
        if n == 1000:
            return 1

        commas = 0
        step = 0
        n_ = 1000
        while n_ < n:
            step += 1
            n_ *= 1000

        while n > 0:
            if step > 0:
                commas += (n // 1000 - 1) * 1000 ** step
            commas += n % (1000 ** step)
            step -= 1
            n = floor(n % 1000 ** step)

        if commas > 0:
            commas += 1
        return commas




s = SolutionDirty()
print(s.countCommas(1024))  # 25
print(s.countCommas(2019))  # 1020
print(s.countCommas(1000))  # 1
print(s.countCommas(998))  # 0

