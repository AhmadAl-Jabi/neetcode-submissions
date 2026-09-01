class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # non recursive approach is actually quite simple

        next_1, next_2 = 0 , 0
        # [1,2,3] n1 n2
        # [1,2,3 (n1)] n2
        # [1,2 (n1),3 (n2)]

        for i in range(len(cost) - 1, -1, -1):
            cost[i] = cost[i] + min(next_1,next_2)
            next_2 = next_1
            next_1 = cost[i]
        
        return min(cost[0],cost[1])
