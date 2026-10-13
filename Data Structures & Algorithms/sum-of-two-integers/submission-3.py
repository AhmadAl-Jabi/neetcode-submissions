class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Problem
        # a and b are just integers -> [-1000,1000]
        # return an integer WITHOUT using + or - --> are we allowed to use methods like sum()
        # we'd have to resort to using bit operations 
        # need to deal with the sign of negative numbers as well

        # a = 5 b = 3 --> return 8
        # a = -5 b = -3 -> return -8

        # we'll need to deal with adding the bits but also carry ons --> 1010 0010 -> 1110
        # XOR to add the bits without carrying -> 0 1 = 1, 0 0 = 0, 1 1 = 0 carry 1
        # AND to find the carry from two bits (since only 1 1 will produce carry of 1)
        bit_mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        carry = ((a & b) << 1) & bit_mask
        result = (a ^ b) & bit_mask

        while carry:
            next_result = (result ^ carry) & bit_mask
            next_carry = ((result & carry) << 1) & bit_mask

            result = next_result
            carry = next_carry
        
        return result if result <= max_int else ~(result ^ bit_mask)
            
            