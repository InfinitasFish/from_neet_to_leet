from __future__ import annotations


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        prod = 1
        n_ = n
        while n_ > 0:
            digit = n_ % 10
            sum += digit
            prod *= digit
            n_ //= 10

        return n % (sum + prod) == 0


s = Solution()
print(s.checkDivisibility(99))  # True

