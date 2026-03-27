from __future__ import annotations


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit


print(Solution().maxProfit([10,1,5,6,7,1]))
print(Solution().maxProfit([10,8,7,5,2]))
