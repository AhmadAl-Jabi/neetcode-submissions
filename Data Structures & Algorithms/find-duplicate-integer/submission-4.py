class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Constraints
        # The biggest number will be len - 1 --> This lets us zero index the original array easily

        # Method
        # Track what we've seen by modifying the array and making the numbers negatives if seen already. 
        # Issue --> This will cause us to modify og so it won't work with the follow up

        # ex: [1,2,3,2,2] --> 0-index it to be [1,-2,3,4,5]

        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val -1] < 0:
                return val
            
            nums[val - 1] *= -1
            
