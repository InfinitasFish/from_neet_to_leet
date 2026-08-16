from __future__ import annotations


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pref = []
        for i in range(len(min(strs, key=lambda x: len(x)))):
            chars = [s[i] for s in strs]
            if len(set(chars)) == 1:
                pref.append(chars[0])
            else:
                break

        return ''.join(pref)


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))  # fl
    print(s.longestCommonPrefix(["dog","racecar","car"]))  # ""


