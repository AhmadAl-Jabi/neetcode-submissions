class Solution:
    def countBits(self, n: int) -> List[int]:
        output_arr = []

        for i in range(n+1):
            count = 0
            digit = i
            while digit:
                count += digit & 1
                digit >>= 1

            output_arr.append(count)
        
        return output_arr