from __future__ import annotations


class Solution:
    # list of strings to one string
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}|{s}"

        return encoded_string

    # string to list of strings
    def decode(self, es: str) -> List[str]:
        decoded_strings = []
        left = 0
        while left < len(es):
            length = ""
            # get length of string
            while ord('0') <= ord(es[left]) <= ord('9'):
                length += es[left]
                left += 1

            # check for delimiter
            if es[left] != '|':
                raise ValueError("Bad encoded string")
            left += 1

            # get string of found length
            decoded_strings.append(es[left:left + int(length)])
            left += int(length)

        return decoded_strings


ts = [
    ["Hello","World"],
    ["", ""],
    ["|||||||||||||||||", "&&&&&&&&||||||$$$$"]
]
s = Solution()
for t in ts:
    res = s.decode(s.encode(t))
    print(f"{t} == {res} : {t == res}")