class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        pro=0
        for i in prices:
            buy=min(buy,i)
            pro=max(pro,i-buy)

        return pro

    
 