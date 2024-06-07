class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left, right = 0, 1
        # maxProfit = 0

        # while right < len(prices):
        #     if prices[left] < prices[right]:
        #         profit = prices[right] - prices[left]
        #         maxProfit = max(maxProfit, profit)
        #     else: 
        #         left = right
        #     right += 1
        
        # return maxProfit


        mProfit=0
        bPrice=prices[0]
        for i in range(1,len(prices)):
            if bPrice > prices[i]:
                bPrice=prices[i]
            else:
                mProfit=max(mProfit,prices[i]-bPrice)
        return mProfit