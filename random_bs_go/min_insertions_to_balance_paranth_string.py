from __future__ import annotations


class Solution_:
    def minInsertions(self, s: str) -> int:
        # valid is "())", left closed by two consecutive right
        # my orig solution, four cases for encountering ')' (2 for empty stack, 2 for non-empty), pretty slow
        stack = []
        res = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(1)
                i += 1
            elif s[i] == ')':
                if len(stack) > 0:
                    if i + 1 == len(s) or s[i + 1] != ')':
                        res += 1
                        i += 1
                    else:
                        i += 2
                    stack.pop()
                else:
                    if i + 1 == len(s) or s[i + 1] != ')':
                        res += 2
                        i += 1
                    else:
                        res += 1
                        i += 2

        res += len(stack) * 2
        return res


class Solution:
    def minInsertions(self, s: str) -> int:
        # something faster, counting without stack
        # pretty hard to visualize
        # 'p' only keep amount of ')' we need to balance string
        # 'k' keep amount of '(' AND amount of SINGLE ')' that we need to balance string
        p = 0
        k = 0
        for i in range(len(s)):
            if s[i] == '(':
                # we need two ')' to balance it
                p += 2
                # if ')' is odd, it means at some point we encountered '()(',
                # so we balance it to '())(' by incrementing 'k' and decrementing 'p' so
                # we won't over-count result in the next steps
                if p % 2 == 1:
                    k += 1
                    p -= 1
            else:
                # simple decrement
                p -= 1
                # if count of needed ')' became negative - we don't have enough '(',
                # so we increment 'k' by one and 'p' by two, so -1 becomes 1, because we need one more ')'
                # ex ')' should become "())" to be balanced, so k = 1 and p = 1
                if p < 0:
                    k += 1
                    p += 2

        return p + k


s = Solution()
print(s.minInsertions("(()))"))  # 1
print(s.minInsertions("))())("))  # 3
print(s.minInsertions("(())((())))))())))")) # 0
print(s.minInsertions("))(")) # 3
print(s.minInsertions(")("))  # 4
