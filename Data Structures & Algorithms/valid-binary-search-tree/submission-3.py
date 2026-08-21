# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #Simple
        # define a nested dfs func, create the recursive logic and base cases
        # pass lows and highs to enforce allowed values (based on the parent node)
        # call this func and just return its output

        def dfs(node, low, high):

            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            # The bounds low and high are EXCLUSIVE. So NOT <= or >=. 
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
            return (left and right)
        
        return dfs(root, -1000, 1000)
        