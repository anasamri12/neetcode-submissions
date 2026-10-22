class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > 0:
                    total.append(profit)
                else:
                    continue
        if not len(total):
            return 0
        else:
            return max(total)
