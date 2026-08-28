from __future__ import annotations


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # balright
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        neg = (divisor < 0 or dividend < 0) and not (divisor < 0 and dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            return dividend if not neg else -dividend
        if dividend == divisor:
            return 1 if not neg else -1

        # instead of just counting num of divisors in dividend,
        # we find the largest double of divisor that <= dividend
        # like dividend >= divisor * 2^p
        # then we subtract dividend -= divisor * 2^p and repeat
        count = 0
        while dividend >= divisor:
            two_p = 0
            while dividend >= divisor << two_p:
                two_p += 1

            two_p -= 1
            count += 1 << two_p
            dividend -= divisor << two_p

        return count if not neg else -count


if __name__ == "__main__":
    s = Solution()
    print(s.divide(10, 3))  # 3
    print(s.divide(7, -3))  # -2
    print(s.divide(-1, 1))  # -1
    print(s.divide(-1, -1))  # 1

