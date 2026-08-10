class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # index = count, value at index = number itself

        num_of_buckets = len(nums) + 1
        buckets = [[] for i in range(num_of_buckets)]

        counts = {}
        out_arr = []

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        for num, count in counts.items():
            buckets[count].append(num)

        for i in range(len(buckets)):
            for j in range(len(buckets[i])):
                out_arr.append(buckets[i][j])

        return out_arr[-1:(-1 - k):-1]




        