class Solution:
    def countBits(self, n: int) -> List[int]:
        output_arr = [0] * (n + 1)

        for i in range(n+1):
            output_arr[i] = output_arr[i >> 1] + (i & 1)
        
        return output_arr