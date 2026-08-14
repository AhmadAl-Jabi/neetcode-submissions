class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # hold a max_profit = 0 variable
        max_profit = 0

        # start left and right pointers at the beginning
        left, right = 0, 0

        # while right is less than len(prices) (big condition)

        while right < len(prices):
        
        
            # if prices[left] is >= than prices[right]
            if prices[left] >= prices[right]:
                left = right
                
         
         # else
            else:
                curr_profit = prices[right] - prices[left]

                if curr_profit > max_profit:
                    max_profit = curr_profit

            right += 1
        
        return max_profit
        