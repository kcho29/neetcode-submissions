class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                cur = max(cur,prices[j]-prices[i])
        return cur
        