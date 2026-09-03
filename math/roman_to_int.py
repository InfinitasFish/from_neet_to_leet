from __future__ import annotations


class SolutionSlow:
    def romanToInt(self, s: str) -> int:
        # 1 <= num <= 3999
        symbol_to_value = {"M": 1000, "D": 500, "C": 100, "L": 50,
                           "X": 10, "V": 5, "I": 1}

        # iterate through single characters and add values accordingly
        # if next character is larger than previous -> subtract form
        result = symbol_to_value[s[0]]
        for i, char in enumerate(s[1:], start=1):
            val = symbol_to_value[char]
            prev = symbol_to_value[s[i - 1]]
            if val > symbol_to_value[s[i - 1]]:
                result = result -  2 * prev + val
            else:
                result += val

        return result


class Solution:
    def romanToInt(self, s: str) -> int:
        # 1 <= num <= 3999
        symbol_to_value = {"M": 1000, "D": 500, "C": 100, "L": 50,
                           "X": 10, "V": 5, "I": 1}

        # additional optimization using two pointers
        result = 0
        for a, b in zip(s, s[1:]):
            if symbol_to_value[a] < symbol_to_value[b]:
                result -= symbol_to_value[a]
            else:
                result += symbol_to_value[a]

        result += symbol_to_value[s[len(s) - 1]]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("VIII"))  # 8
    print(s.romanToInt("MCMXCIV"))  # 1994
