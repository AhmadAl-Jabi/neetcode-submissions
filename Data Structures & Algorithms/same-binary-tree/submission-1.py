# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # what do two trees need to be considered the same tree:
        # exact same structure (for each node, is its .left and .right the same as the other tree's corresponding node)
        # exact same values (then nodes must have the same .val ints)

        # base case when we hit none (both effectively same tree)
        if not p and not q:
            return True
        
        # if only one of them is none we return false (before we checked if BOTH are none, so this only gets checked if that wasn't the case)
        if not p or not q:
            return False

        # recursive step of checking if val is same
        if p.val != q.val:
            return False    

        # the idea is that we call "isSameTree" on all the nodes and consider even the leafs of both trees as trees themselves. If at any point there is a discrepency we return False
        left_trees = self.isSameTree(p.left, q.left)
        right_trees = self.isSameTree(p.right, q.right)

        return left_trees and right_trees # both need to be true
        

