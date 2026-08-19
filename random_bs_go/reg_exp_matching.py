# they say it's hard problem
from __future__ import annotations


# true solution utilises 2d dynamic programming
# I can't grasp it for now, so ill return after solving some easier DP problems:
# todo: do dp


# of course pure logic doesn't work here, wasting my time
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         # patterns are only '.' (one char) and '*' (zero or more preceding) with letters
#         is_match = True
#         no_tail = False
#         skip = False
#         min_match = sum([1 for char in p if char != '*'])
#         match_count = 0
#         l = 0
#         n = len(s)
#         for i, pa in enumerate(p):
#             if skip:
#                 skip = False
#                 continue
#
#             if l >= n and pa != '*':
#                 return False
#
#             if pa == '.':
#                 if l < n:
#                     l += 1
#                     match_count += 1
#                 else:
#                     return False
#
#             elif pa == '*':
#                 # guaranteed to have char before '*'
#                 while l < n and s[l] == s[l - 1]:
#                     l += 1
#
#             else:
#                 if s[l] != pa:
#                     if i + 1 < len(p) and p[i + 1] == '*':
#                         min_match -= 1
#                         skip = True
#                         continue
#                     else:
#                         return False
#                 l += 1
#                 match_count += 1
#
#         if match_count >= min_match:
#             no_tail = True
#
#         return is_match and no_tail


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))  # False
    print(s.isMatch("aa", "a*"))  # True
    print(s.isMatch("ab", ".*"))  # True
    print(s.isMatch("hellloworldd", "hel*..or.d*"))  # True
    print(s.isMatch("hellloworld", "hel*..or.d*"))  # True
    print(s.isMatch("hellloworl", "hel*..or.d*"))  # False
    print(s.isMatch("heloworld", "hel*..or.d*"))  # True
    print(s.isMatch("aab", "c*a*b"))  # True
    print(s.isMatch("mississippi", "mis*is*p*."))  # False
