from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lower_k = 1
        upper_k = max(piles)
        best_k = 0
        #k_min_not_found = True

        #Can maybe do binary search on the values of k and have an upper bound for k (which would simply be the max pile size. It will never be bigger than this)

        # Some Notes:
        # h is hours but it's more constructive to think of it as the number of times we can subtract from a stack of bananas
        # len(piles) is the number of stacks we have
        # k is the number we subtract from one stack for each iteration of h (for each hour)

        # The goal is to minimize k as much as possible and have an empty pile at h >= 0
        # We can keep going till piles is either empty (removed all bananas) or we finish iterating h and piles not empty
        # For each iteration we can check piles is empty, and if not then if piles[-1] is 0 or negative after removing the bananas and pop it
        
        # Now how do we go about optimizing the k? 

        while lower_k < upper_k: # We either keep going till we find ideal case (h_needed == h) or we've exhausted our options

            mid_k = (lower_k + upper_k) //2
            h_needed = 0

            for pile in piles:
                h_needed += ceil(pile/mid_k) 

            # After checking how long it takes we see if we can still decrease k or not. Just cuz it worked doesn't mean it's best
            # If h_needed == h then we might still be able decrease k (for example if it's smt like [2,2,4] and k=3 gave us h_needed == h, so can k=2)
            
            if h_needed > h: # k too small
                lower_k = mid_k + 1
            
            else: # k too big or maybe can try one more
                upper_k = mid_k

        return lower_k 


        