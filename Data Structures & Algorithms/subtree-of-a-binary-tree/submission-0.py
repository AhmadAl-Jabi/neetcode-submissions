# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Basically make a function that checks if both trees are currently the same thru dfs
        # Can return true if we good
        # Otherwise we just keep going and calling it but we move the og tree left and right
       
        if not root:
            return False

        def isSameTree(node1, node2):
            # Do full recursive dfs search here
            if (not node1 and not node2):
                return True

            if (not node1 and node2) or (not node2 and node1) or (node1.val != node2.val):
                return False
            
            return isSameTree(node1.left,node2.left) and isSameTree(node1.right,node2.right)


        return (root.val == subRoot.val and isSameTree(root,subRoot)) or (self.isSubtree(root.left,subRoot)) or (self.isSubtree(root.right,subRoot))