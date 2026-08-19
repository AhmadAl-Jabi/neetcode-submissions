# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is not same as height (diameter not necessarily through root)
        self.max_diameter = 0
        def findDiameterOfTree(node):
            # base case
            if not node:
                return -1 # if we hit none then it's a negative diameter (single node is diameter 0)
            
            left_diameter = findDiameterOfTree(node.left)
            right_diameter = findDiameterOfTree(node.right)

            curr_diameter = (left_diameter + right_diameter) + 2
            self.max_diameter = curr_diameter if self.max_diameter < curr_diameter else self.max_diameter

            return max(left_diameter, right_diameter) + 1
        
        findDiameterOfTree(root)
        return self.max_diameter
        