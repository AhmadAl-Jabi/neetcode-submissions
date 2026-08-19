# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        
        def checkHeight(node):
            # left and right subtree height diff can't be > 1
            if not node:
                return -1
            
            left_height = checkHeight(node.left)
            right_height = checkHeight(node.right)

            if abs(left_height - right_height) > 1:
                self.isBalanced = False

            return max(left_height, right_height) + 1
        
        checkHeight(root)
        return self.isBalanced

    
    
        