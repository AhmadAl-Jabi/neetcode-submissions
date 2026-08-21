# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #Thought process is to create another func (dfs)
        # Where we can keep calling it recursively
        # At each node we check the current diameter thru left and right recursion

        # Base case if null then return -1
        # Then we go left and right and store left height and right height
        # Then we take the max of the two and add 1 to it
        # we store a best diameter var where we update it if the current node has a bigger diameter
        best = 0

        def dfs(node):
            nonlocal best

            if not node:
                return -1
            
            lh = dfs(node.left)
            rh = dfs(node.right)
 
            best = max(best, lh + rh + 2) # Calculate current diameter 

            return 1 + max(lh,rh) # This is to tell us which route to try next based on depth

        dfs(root)
        return best


        