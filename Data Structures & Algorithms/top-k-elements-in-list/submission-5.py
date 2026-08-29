class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output_arr = []
        freq_map = {}
        counter = 0

        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1

        buckets = [[] for i in range(len(nums) + 1)] # len(nums) + 1 since if [1,1,1] --> index 3 would need [0] [1] [2] [3] would need 4 buckets (len(nums) + 1)

        for key in freq_map:
            frequency = freq_map[key]
            buckets[frequency].append(key)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if counter == k:
                    break

                output_arr.append(num)
                counter += 1
        
        return output_arr

        
        