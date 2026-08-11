import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # piles tells us how many bananas need to be eaten in each pile
        # minimum 1 hour per pile (can take longer if piles[i] > k)
        # we want the SMALLEST possible k that lets us finish in h hours

        # How do we determine how many hours it takes us?
        # can do piles[i] / k  and just round up
        # then we add to a global counter of total_hours

        # How do we decide best k?
        # We can have binary search of candidates from 1 to max(piles)
        # we take the middle each time
        # if it takes MORE than h hours --> left = mid + 1
        # if it takes h hours or LESS --> right = mid --> if k took h hours it is not necessarily the best solution (there could be a smaller k) so group condition

        # we can stop and return our k when left > right

        left, right = 1, max(piles)

        while left < right:

            mid = (left + right) // 2 # the index
            hours_taken = 0

            for bananas in piles:
                hours_taken += math.ceil(bananas / mid)
            
            if hours_taken > h:
                left = mid + 1
            
            else:
                right = mid 
        
        return left

        