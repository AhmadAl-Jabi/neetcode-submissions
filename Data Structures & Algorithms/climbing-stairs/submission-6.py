class Solution:
    def climbStairs(self, n: int) -> int:
        # Main thing to realize is that ways(n) = ways(n-1) + ways(n-2) --> Quite simple actually
        # All we want is the NUMBER of ways, not the sequences themselves

        ways_minus_2 = 1 # When we start with n = 2 --> Our formula above only applies n >= 2 (like fibonnaci). n = 0,1 are base cases
        ways_minus_1 = 1

        for i in range(n-1):
            temp = ways_minus_1
            ways_minus_1 += ways_minus_2
            ways_minus_2 = temp

        return ways_minus_1 # If n = 1 the loop does not execute and we return 1 (base case). We don't need to worry about case n = 0
        
        