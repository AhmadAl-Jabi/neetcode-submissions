class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in cache: # If this amount was already seen in our cache
                return cache[amount]

            
            result = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    result = min(result,1 + dfs(amount - coin))
            
            cache[amount] = result # Basically saying that at this amount the lowest num of coins is result
            # If none of the 4 coins can let us go lower that means it's a dead end and we will store inf
            # In the end if we return inf then we know to return -1

            return cache[amount]
        
        num_of_coins = dfs(amount)
        if num_of_coins >= 1e9:
            return -1
        else:
            return num_of_coins
