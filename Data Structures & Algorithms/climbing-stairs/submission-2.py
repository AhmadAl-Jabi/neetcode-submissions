class Solution:
    def climbStairs(self, n: int) -> int:
        # Main thing to realize is that ways(n) = ways(n-1) + ways(n-2) --> Quite simple actually
        # All we want is the NUMBER of ways, not the sequences themselves

        n_minus_2 = 1
        n_minus_1 = 1

        for i in range(n):
            temp = n_minus_1
            n_minus_1 += n_minus_2
            n_minus_2 = temp

        return n_minus_2
        
        