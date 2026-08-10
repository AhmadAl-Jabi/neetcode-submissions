class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

    # Basic approach is to just get the product of all numbers (total)
    # and then for each number just divide total by said number
    # But how do we deal with 0 (product will be 0 and div by 0 is bad)

    # If no 0's then we're good
    # If 1 zero then calculate total w/o it 
    # If 2+ zeros then always 0
        total = 1
        zero_count = 0
        output = [0] * len(nums)

        for num in nums:
            if num == 0:
                zero_count += 1
            total *= num # If no zeros we'll get correct total

        if zero_count == 0:
            for i in range(len(nums)):
                output[i] = int(total/nums[i])
        
        elif zero_count == 1:
            zero_index = 0
            total = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    total *= nums[i]
                    output[i] = 0
                else:
                    zero_index = i
            output[zero_index] = total
        
        return output

        