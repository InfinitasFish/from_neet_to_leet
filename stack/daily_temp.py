from __future__ import annotations


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        until_warmer = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                j, _ = stack.pop()
                until_warmer[j] = i - j
            stack.append((i, temperatures[i]))

        return until_warmer


ts1 = [30,38,30,36,35,40,28]  # [1,4,1,2,1,0,0]
print(Solution().dailyTemperatures(ts1))
ts2 = [22, 21, 20]  # [0,0,0]
print(Solution().dailyTemperatures(ts2))
