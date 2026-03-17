from __future__ import annotations

import time
from math import floor, ceil

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # problem assumes that there are only valid expressions
        stack_ints = []
        for i, token in enumerate(tokens):
            # check whether int of op
            try:
                it = int(token)
                stack_ints.append(it)
            except Exception:
                it2, it1 = stack_ints.pop(), stack_ints.pop()
                match token:
                    case '+':
                        stack_ints.append(it1 + it2)
                    case '-':
                        stack_ints.append(it1 - it2)
                    case '*':
                        stack_ints.append(it1 * it2)
                    case '/':
                        t = it1 / it2
                        if t < 0:
                            stack_ints.append(ceil(t))
                        else:
                            stack_ints.append(floor(t))

        return stack_ints.pop()


#tokens=["4","13","5","/","+"]
# 9 + 3 ;
# 12 * -11 ;
# 6 / -132 ;
# 10 * 0 ;
# 0 + 17
# 17 + 5 -> 22
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))


