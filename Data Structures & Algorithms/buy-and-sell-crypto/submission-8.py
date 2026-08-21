class Solution:
    def maxProfit(self, prices: List[int]) -> int:

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
            
        