class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # We want the NUMBERS not the indices
        # No duplicate triplets but within a triplet you can have a number show up many times

        out_arr = []

        # We have 3 indices i, j, k.
        # I'm thinking we delegate i to be the marching index that closes the possible options as we loop
        # Start i at 0 and then everytime it moves up we ignore everything left of i
        
        # We SORT the array first and foremost so that two pointer can even work

        # Do basic two pointer approach but keep going until j and k meet/overlap
        # When they do meet we just advance i easy peezy

        i = 0
        nums.sort()
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            
            # Don't want overlap
            while j < k:

                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    continue
                
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    continue
                
                if [nums[i],nums[j],nums[k]] not in out_arr:
                    out_arr.append([nums[i],nums[j],nums[k]])
                
                j += 1
                k -= 1
                
            i += 1
        
        return out_arr
                    
                
