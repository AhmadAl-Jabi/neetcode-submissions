# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # In order to find a descendant we can use the fact that its a bst and only need to make one move at each depth
        # If child bigger than curr node, go right
        # If child smaller than, go left

        # We do NOT need to worry about whether or not the nodes exist. We take that for granted
        # So it's really a matter of ending the function at the latest possible node we can

        # We go until we reach a point where there is a divergence. One node is smaller than the parent, the other is bigger
        # This tells us that we cannot possibly go further as this is the last parent of both

        while  (root.val > max(p.val,q.val)) or (root.val < min(p.val,q.val)):

            if root.val > max(p.val,q.val):
                root = root.left
            
            else:
                root = root.right
        
        return root

        