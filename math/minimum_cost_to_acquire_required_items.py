from __future__ import annotations


class Solution_:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # simple strategy, time limit exceeds, O(n+m)
        res = 0
        while need1 > 0 and need2 > 0:
            if cost1 + cost2 < costBoth:
                res += cost1 + cost2
            else:
                res += costBoth

            need1 -= 1
            need2 -= 1

        while need1 > 0:
            if costBoth < cost1:
                res += costBoth
                need2 -= 1
            else:
                res += cost1
            need1 -= 1

        while need2 > 0:
            if costBoth < cost2:
                res += costBoth
            else:
                res += cost2
            need2 -= 1

        return res


class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # calculating without cycles, so constant time O(1)
        res = 0
        if need1 > need2:
            need1, need2 = need2, need1
            cost1, cost2 = cost2, cost1

        if cost1 + cost2 > costBoth:
            res += need1 * costBoth + (need2 - need1) * min(costBoth, cost2)
        else:
            res += need1 * cost1 + need2 * cost2

        return res



s = Solution()
print(s.minimumCost(3,2,1,3,2))  # 3
print(s.minimumCost(5,4,15,2,3))  # 22
print(s.minimumCost(93, 31, 32, 3, 10))  # 313
print(s.minimumCost(3,2,1,3,2))  # 3
