from __future__ import annotations


class SolutionSlow:
    def countPrimes(self, n: int) -> int:
        # 0 <= n <= 10^6
        count = 0

        def is_prime(n):
            is_prime = True if n > 1 else False
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
            return is_prime

        for i in range(n):
            if is_prime(i):
                count += 1

        return count


class Solution:
    def countPrimes(self, n: int) -> int:
        # 0 <= n <= 10^6
        # the trick is not to check every number for being prime
        # by marking multiples of found prime numbers, e.g. 2 is prime, we mark 4, 6, 8 up to n as non-prime

        if n <= 2:
            return 0

        # another optimization is based on fact that any even number > 2 isn't prime
        # so we can check from i = 3 and i += 2
        # also in this case we will assume that every odd number is prime, so
        # initial count = n // 2
        count = n // 2
        primes = [True] * n
        primes[0] = False
        primes[1] = False

        i = 3
        while i < n:
            if primes[i]:
                # any smaller multiple of i would have already been marked by smaller prime
                j = i * i
                # a bit faster-than-loop assign
                upd_len = len(primes[j :n :2 * i])
                primes[j :n :2 * i] = [False] * upd_len
            else:
                count -= 1
            i += 2

        return count


s = Solution()
print(s.countPrimes(0))  # 0
print(s.countPrimes(1))  # 0
print(s.countPrimes(3))  # 1
print(s.countPrimes(10))  # 4
print(s.countPrimes(100))  # 25




