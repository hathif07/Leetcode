class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        n =  len(discounts)
        total = 0.0

        for i in range(len(prices)):
            if i < n:
                total+= prices[i] * (100 - discounts[i])/100.0
            else:
                total += prices[i]

        return total