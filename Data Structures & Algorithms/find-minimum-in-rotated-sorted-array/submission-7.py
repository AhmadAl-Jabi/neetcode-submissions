class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Split the array in half and take the middle pointer
        # Basically check the left and right pointers and see which of the two is smaller
        # Then take the left to the middle or middle to the right
        # We don't want to do -1 or +1 tho cuz it'll eliminate potential answers so do while left < right

        # [6,1,2,3,4,5]
        # [5,6,1,2,3,4]
        # [4,5,6,1,2,3]

        left = 0 
        right = len(nums) - 1

        while right > left:
            mid = (left + right)//2

            # Key idea: compare mid to right
            if nums[mid] > nums[right]:

                # min is strictly to the right of mid
                left = mid + 1
                
            else:
                # min is at mid or to the left
                right = mid

        return nums[left]

        