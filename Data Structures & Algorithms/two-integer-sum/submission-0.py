class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complements = {}

        for i in range(len(nums)):
            complement_val = target - nums[i] 

            if nums[i] in complements:
                return [complements[nums[i]], i]
            
            else:
                complements[complement_val] = i
        