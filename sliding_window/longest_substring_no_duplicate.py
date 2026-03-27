from __future__ import annotations


# toxic
class SolutionLessMem:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cur_seq = {}
        max_len = 0
        while left < len(s):
            if s[left] in cur_seq:
                if len(cur_seq) > max_len:
                    max_len = len(cur_seq)

                # clear chars before first char occurrence
                new_seq = {}
                for k, v in cur_seq.items():
                    if v > cur_seq[s[left]]:
                        new_seq[k] = v
                cur_seq = new_seq

            cur_seq[s[left]] = left
            left += 1

        if len(cur_seq) > max_len:
            max_len = len(cur_seq)

        return max_len


# humanly
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # so better way to remove anything before duplicate is to
        # move some left pointer until duplicate will be deleted
        char_set = set()
        l = 0
        max_len = 0
        for r in range(len(s)):
            while s[r] in char_set:
                max_len = r - l if r - l > max_len else max_len
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])

        max_len = len(s) - l if len(s) - l > max_len else max_len

        return max_len

print(Solution().lengthOfLongestSubstring("zxyzxyz"))  # 3
print(Solution().lengthOfLongestSubstring("xxxxx"))  # 1
print(Solution().lengthOfLongestSubstring("xyzywzzzz"))  # 3

