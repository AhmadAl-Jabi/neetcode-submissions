# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # We never deal with none nodes (since root isn't none)

        # We'll need to send a range of allowed values each call (min,max) that starts -inf,+inf --> when we move left we update right side of range to be root.val -1, when move right we update left side for range to be root.val + 1
        def checkBST(node, range):
            # just check curr node is in correct range --> if not return False
            if node.val > range[1] or node.val < range[0]:
                return False
            
            # We say else True since if we have no kids by default its a valid BST
            left_tree = checkBST(node.left,[range[0],node.val - 1]) if node.left else True
            right_tree = checkBST(node.right,[node.val + 1, range[1]]) if node.right else True

            return left_tree and right_tree
        
        return checkBST(root,[float("-inf"),float("inf")])

        
        