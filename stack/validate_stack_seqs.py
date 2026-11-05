from __future__ import annotations


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        # popped.length == pushed.length
        # original but kinda slow
        s = []
        pop_idx = 0
        for i in range(len(pushed)):
            # keep current pushed stack
            s.append(pushed[i])
            # if item is poppable, pop as many items as possible
            if pushed[i] == popped[pop_idx]:
                while len(s) and pop_idx < len(popped) and s[-1] == popped[pop_idx]:
                    s.pop()
                    pop_idx += 1

        # check any residual items
        while len(s) and pop_idx < len(popped) and s[-1] == popped[pop_idx]:
            s.pop()
            pop_idx += 1

        return len(s) == 0


s = Solution()
print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))  # True
print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))  # False
print(s.validateStackSequences([2,1,0], [1,2,0]))  # True
