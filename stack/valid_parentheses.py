from __future__ import annotations


class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        stack = Stack()
        mirror_par_map = {'{': '}', '[': ']', '(': ')'}
        for par in s:
            if par in mirror_par_map:
                stack.add(par)
            else:
                last = stack.pop()
                if last is None or mirror_par_map[last] != par:
                    return False

        return stack.len() == 0


class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def add(self, it):
        self.stack.append(it)
        self.count += 1

    def pop(self):
        if self.count > 0:
            last = self.stack[-1]
            self.stack = self.stack[:-1]
            self.count -= 1
            return last
        return None

    def len(self):
        return len(self.stack)


d_ss = {'[]': True, '([{}])': True, '[(])': False}
s = Solution()
for ss, gt in d_ss.items():
    r = s.isValid(ss)
    if not s.isValid(ss) == gt:
        print(f'git gud, {ss}: exp. {gt} != act. {r}')
        break
