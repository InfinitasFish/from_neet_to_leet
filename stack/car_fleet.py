from __future__ import annotations


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), key=lambda k: k[0])
        times = [(target - combined[i][0]) / combined[i][1] for i in range(len(position))]

        stack = [times[0]]
        for i in range(1, len(times)):
            while stack and stack[-1] <= times[i]:
                stack.pop()
            stack.append(times[i])

        return len(stack)


print(Solution().carFleet(10, [1, 4], [3, 2]))  # 1
print(Solution().carFleet(10, [4,1,0,7], [2,2,1,1]))  # 3
print(Solution().carFleet(10, [1, 3, 7], [8, 1, 2]))  # 2
print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]))  # 1
print(Solution().carFleet(10, [8,3,7,4,6,5], [4,4,4,4,4,4]))  # 6