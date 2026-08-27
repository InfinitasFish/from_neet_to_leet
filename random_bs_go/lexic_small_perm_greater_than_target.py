from __future__ import annotations


class SolutionMem:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        assert len(s) == len(target)

        # hits memory limit, but works
        def perm(str, step, res):
            if len(str) == 0:
                res.append(step)

            for i in range(len(str)):
                perm(str[:i] + str[i + 1:], step + str[i], res)

        perms = []
        perm(s, '', perms)
        candidates = [p for p in perms if p > target]
        return min(candidates) if candidates else ''


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        assert len(s) == len(target)

        # todo: don't write an 'explanation' before solving the problem next time....
        # for smallest perm difference should be as far right as possible
        # after placing difference at [i], we put remaining characters in ascending order

        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(s)
        matched = 0

        while matched < n and count[ord(target[matched]) - ord('a')] > 0:
            count[ord(target[matched]) - ord('a')] -= 1
            matched += 1

        start = matched if matched < n else n - 1

        for i in range(start, -1, -1):
            if i < matched:
                count[ord(target[i]) - ord('a')] += 1

            bigger = -1
            for ch in range(ord(target[i]) - ord('a') + 1, 26):
                if count[ch] > 0:
                    bigger = ch
                    break

            if bigger != -1:
                count[bigger] -= 1

                answer = target[:i] + chr(ord('a') + bigger)

                for ch in range(26):
                    answer += chr(ord('a') + ch) * count[ch]

                return answer

        return ""


s = Solution()
print(s.lexGreaterPermutation("z", "z"))  # ""
print(s.lexGreaterPermutation("aab", "aba"))  # baa
print(s.lexGreaterPermutation("abc", "bba"))  # bca
print(s.lexGreaterPermutation("leet", "code"))  # eelt
print(s.lexGreaterPermutation("baba", "bbaa"))  # ""
print(s.lexGreaterPermutation("abb", "bab"))  # bba
print(s.lexGreaterPermutation("ab", "ab"))  # ba
print(s.lexGreaterPermutation("ab", "aa"))  # ab


