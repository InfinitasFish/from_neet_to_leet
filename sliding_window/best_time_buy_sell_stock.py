from __future__ import annotations


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price_t in prices[1:]:
            if price_t - min_price > max_profit:
                max_profit = price_t - min_price
            if price_t < min_price:
                min_price = price_t

        return max_profit


print(Solution().maxProfit([10,1,5,6,7,1]))
print(Solution().maxProfit([10,8,7,5,2]))
