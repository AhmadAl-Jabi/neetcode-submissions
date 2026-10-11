class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # we know that any number XOR with itself is 0
        '''
        X Y XOR
        0 0 0
        0 1 1
        1 0 1
        1 1 0
        
        6 XOR 6
        0110 XOR 0110 = 0000
        '''
        # anything XOR 0 is itself
        result = 0

        for num in nums:
            result = result ^ num
        
        return result