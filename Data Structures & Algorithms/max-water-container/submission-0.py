class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The amount of water is basically the heigh of the shorter of the two
        # Times the space between both (length x width)
        # length is just index_2 - index_1

        # We just want to return the area. Issue is we need a way to do this without testing every possibility

        # I think what we can do is just start at both ends, calculate area
        # and then move the one with the smaller height left or right (depends on side)
        # and we constantly update max area

        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            curr_area = min(heights[left],heights[right]) * (right - left)

            if curr_area > max_area:
                max_area = curr_area
            
            if heights[left] > heights[right]:
                right -= 1
            
            else:
                left += 1

        return max_area


        