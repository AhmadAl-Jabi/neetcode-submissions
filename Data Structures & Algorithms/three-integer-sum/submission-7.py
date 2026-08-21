class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # ex: [-4,-1,-1,0,1,2]
        three_sums = []

        # k is the target that keeps changing --> need i + j + k == 0 --> i + j == -k
        for k in range(len(nums)):
            
            # This just ensures that we don't have any dupe cases of k values
            if k > 0 and nums[k - 1] == nums[k]:
                continue

            last_idx = len(nums) - 1 
            i = k + 1 # THIS IS IMPORTANT. This is what allows us to avoid any dupes. Start i to the right of k
            j = last_idx

            while i < j:

                target = -nums[k]
                val = nums[i] + nums[j]

                if (val) < target: # might have to adjust sign of k
                    i += 1
                
                elif (val) > target:
                    j -= 1

                else: # So we hit the point where we have a match
                    three_sums.append([nums[i],nums[j],nums[k]])

                    old_i = nums[i]
                    old_j = nums[j]

                    while i < j and nums[i] == old_i:
                        i += 1
                    while i < j and nums[j] == old_j: # Technically don't need this part for moving j left but I prefer to have it
                        j -= 1
                    
        return(three_sums)

                
        # We can think of this problem as a normal two pointer where the target is the negative of the third number
        