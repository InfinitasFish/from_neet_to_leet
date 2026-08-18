from __future__ import annotations


# my orig solution, beats 100% runtime (though 94% solutions have the same 0ms)
class Solution:

    digits_map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                  '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        # 2 <= digit <= 9
        # any order in result

        if len(digits) == 1:
            return [char for char in self.digits_map[digits[0]]]

        result = []
        res_hat = self.letterCombinations(digits[1:])
        for char in self.digits_map[digits[0]]:
            for comb in res_hat:
                result.append(char + comb)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(s.letterCombinations("2"))  # ["a", "b", "c"]
    print(s.letterCombinations("234"))  # ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", ...]
