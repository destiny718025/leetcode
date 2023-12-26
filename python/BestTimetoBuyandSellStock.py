class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        m = prices[0]
        for i in range(1, len(prices)):
            m = min(m, prices[i])
            diff = max(diff, prices[i] - m)

        return diff