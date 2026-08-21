# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Will likely have a similar approach to the last one and use dfs

        isBalanced = True # Change to false if ever 

        def dfs(node):
            nonlocal isBalanced

            if not node:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)

            if abs(lh - rh) <= 1:
                return max(lh,rh) + 1
            
            else:
                isBalanced = False
                return max(lh,rh )+1
        
        dfs(root)
        return isBalanced

        