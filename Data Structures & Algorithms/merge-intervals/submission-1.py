class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [1,10] [3,6]
        # non overlapping only if the beginning of the interval that starts "later" is smaller OR equal to end of the first interval
        # however this requires that our intervals array is sorted in order of the first index of each interval
        intervals.sort(key = lambda a: a[0]) # O(nlogn)
        output_arr = [intervals[0]] # initially starts with the first interval

        # after intervals is sorted, all we do is compare the current interval's first index to output_arr[-1]'s second index


        for i in range(1,len(intervals)): 
            last_merged = output_arr[-1]
            # if curr interval's first index is smaller/equal than --> merge the two intervals (i.e. output_arr[-1][1] = max(curr[1], output_arr[-1][1]) (just change the ending of the output_arr second index, don't touch first index)
            if intervals[i][0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], intervals[i][1])

            # else append curr to output_arr
            else:
                output_arr.append(intervals[i])

        # example output_arr = [[1,5]] curr is [3,]
        # example output_arr = [[1,5]] curr is [6, 10]

        # return output_arr
        return output_arr
        