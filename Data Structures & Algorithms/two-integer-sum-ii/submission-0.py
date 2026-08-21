class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This is two sum but we also have that they are 1-indexed and index 1 must be smaller than 2
        # The index-1 thing seems trivial since I can just add 1 to both at the end

        # Can't use hashmap cuz of the O(1) space worst case, but at least it's sorted this time unlike the original two sum
        # So can use a two pointer solution

        out_arr = []

        # Remember to check that the indexes can't be the same
        last_idx = len(numbers) - 1
        i = 0
        
        while i < last_idx:

            j = last_idx

            while i < j:

                if (numbers[i] + numbers[j] != target): 
                    j -= 1
                
                else: 
                    return [i+1,j+1]

            i += 1

        