class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # I'm thinking of maintaining a cost array of each step that would be len(cost) large (init each index with -1)
        cost_arr = [float('inf')] * len(cost)

        def dfs(i):
            # base case when we're index out of bound to return -1
            if i >= len(cost):
                return 0 # we managed to get out so the cost of that is nothing

            # then basically we can do some sort of recursive function where we first check if curr index was computed already
            # if it was that would mean we already found the cheapest option here and we just use it and return it
            if cost_arr[i] != float("inf"):
                return cost_arr[i]

            # otherwise we explore the i + 1 and i + 2 cases 
            option_1, option_2 = dfs(i+1), dfs(i+2)

            # we can take the minimum cost of the two and set cost_arr[i] to be that + the cost of curr
            cost_arr[i] = min(option_1,option_2) + cost[i]
            return cost_arr[i]
        
        dfs(0)
        return min(cost_arr[0],cost_arr[1])