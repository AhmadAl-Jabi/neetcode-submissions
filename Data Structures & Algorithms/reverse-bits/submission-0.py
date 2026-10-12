class Solution:
    def reverseBits(self, n: int) -> int:
        # Understanding
        # unsigned integer n -> reverse bits -> return integer representation
        # we essentially want to mirror the bits from the middle -> last bit becomes first bit so on and so forth
        # we build a new integer from scratch this way

        # going left to right we're just doing 2**i * bit where i is from 31 to 0
        # to get the right most bit we just do n & 1
        # shift n >> 1 each time

        result = 0

        for i in range(31,-1,-1):
            curr_bit = n & 1
            result += (2**i * curr_bit)
            n >>= 1
        
        return result

