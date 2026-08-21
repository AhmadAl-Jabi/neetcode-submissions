# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # I'm thinking of basically doing a search on each node at the same time by checking if their values equate
        # Then recursively do the same with the left and right nodes
        # Have a isSameTree variable that is initially True
        # Can make a nested func to make it cleaner

        isSameTree = True

        def checkNodes(node1, node2):

            nonlocal isSameTree

            if not node1 and not node2:
                return
            
            # If one is null but other isn't then they're automatically unequal
            elif (not node1 and node2) or (not node2 and node1) or (node1.val != node2.val):
                isSameTree = False
                return 
            
            checkNodes(node1.left,node2.left)
            checkNodes(node1.right,node2.right)

        checkNodes(p,q)
        return isSameTree
            
            
            