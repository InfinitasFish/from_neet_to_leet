from __future__ import annotations


# original bad solution
class SolutionSlow:
    def intToRoman(self, num: int) -> str:
        # 1 <= num <= 3999
        # can stack only powers of 10 up to three times
        # can't stack 50 (L), 200 (D)
        result = []
        first_int_map = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                         6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        i = num % 10
        num //= 10
        if i != 0:
            result.append(first_int_map[i])

        pow_to_val = {10: 'X', 100: 'C', 1000: 'M'}
        pow_i = 10

        while num > 0:
            i = num % 10 * pow_i

            if i > pow_i * 3:
                f = 'L' if pow_i == 10 else 'D'
                lead = i // pow_i

                if lead == 4:
                    result.append(pow_to_val[pow_i] + f)

                elif lead == 5:
                    result.append(f)

                elif lead == 9:
                    result.append(pow_to_val[pow_i] + pow_to_val[pow_i * 10])

                else:
                    char = [pow_to_val[pow_i]]
                    mul = lead - 5
                    result.append(f + ''.join(char * mul))

            else:
                char = [pow_to_val[pow_i]]
                mul = i // pow_i
                result.append(''.join(char * mul))

            num //= 10
            pow_i *= 10


        result.reverse()
        return "".join(result)


# fast solution
class Solution:
    def intToRoman(self, num: int) -> str:
        # covers all possible combinations for num <= 3999
        # for bigger numbers we would have to add new symbols,
        # like 4000, 5000, 9000, 10000 etc.
        symbols_map = {1000: 'M', 900: "CM", 500: 'D', 400: "CD",
                       100: 'C', 90: "XC", 50: 'L', 40: "XL", 10: 'X',
                       9: "IX", 5: "V", 4: "IV", 1: 'I'
                       }

        result = []
        for val, char in symbols_map.items():
            if num == 0:
                break
            count = num // val
            result.append(char * count)
            num -= val * count

        return ''.join(result)



if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(1234))  # MCCXXXIV
    print(s.intToRoman(58))  # LVIII
    print(s.intToRoman(1994))  # MCMXCIV
    print(s.intToRoman(3749))  # MMMDCCXLIX

