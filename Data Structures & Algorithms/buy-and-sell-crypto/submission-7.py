class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I would start with left pointer on first num and right pointer right next to it
        # I want to minimize left pointer and maximize right pointer. I can calculate profit as prices[right] - prices[left] at each step
        # and change max if it beats it. Left should always be smaller idx than right
        # if profit is 0 or less then return 0.
        # At each step check if moving left makes it more cheap to buy than moving right makes it more money to sell. Basically prioritize
        # The max profit

        # New attempt --> keep left stationary and keep moving right. Check profit each time I move right. If right sees smt smaller than left
        # (SO a new best buy), make left = right and move right. Keep calculating till right reaches the end

        if len(prices) <= 1:
            return 0

        left = 0
        right = 1
        max_prof = 0

        while right < len(prices):
            prof = prices[right] - prices[left]

            if prof > max_prof:
                max_prof = prof

            if prices[right] < prices[left]:
                left = right

            right += 1
            
        return max_prof
            
        