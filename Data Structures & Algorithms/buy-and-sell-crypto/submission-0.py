class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = prices[0]
        r = l

        for p in prices:
            if p > r:
                r = p
            elif p < l:
                l = p
                r = p
            
            res = max(res, r - l)
        
        return res 
        