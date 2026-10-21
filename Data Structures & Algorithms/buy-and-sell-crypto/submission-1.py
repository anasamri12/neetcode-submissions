class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        comb = []
        for i in range(len(prices)):
            for y in range(i + 1, len(prices)):
                if prices[i] > prices[y]:
                    continue
                else:
                    comb.append(prices[y] - prices[i])
        
        print(comb)
        if comb:
            return max(comb)
        else:
            return 0
