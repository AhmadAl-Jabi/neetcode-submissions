class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_array = [1] * len(nums)

        # Forward pass. Fix the prefixes
        forward_total = 1
        for i in range(len(nums)):
            product_array[i] = forward_total
            forward_total *= nums[i]

        # Backward pass. Fix the suffixes
        backward_total = 1
        for i in range(len(nums))[::-1]:
            product_array[i] *= backward_total
            backward_total *= nums[i]

        # Return the output array
        return product_array