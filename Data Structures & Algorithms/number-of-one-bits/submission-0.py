class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        00010111 = 23
        00000001
        4 1s

        '''

        count = 0

        while n != 0:
            count += n & 1
            n >>= 1
        return count