# easy question, so what


class Solution:
    def isUgly(self, n: int) -> bool:
        # ugly number is positive integer that only have these prime factors: 2, 3, 5
        # or none of them at all
        if n <= 0:
            return False

        if n == 1:
            return True

        # the idea is to just divide number by 2, 3 and 5 while possible
        # if we can't divide without a tail -> return False
        while n > 1:
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False

        return True


s = Solution()
print(s.isUgly(6))  # True
print(s.isUgly(14))  # False
