# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # root = 5, p = 1, q = 4
        #  5
        # 3  8
        #1 4 7 9
        #2
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)

        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        return root

        # Basically check at current root if both p and q are either bigger or smaller than root --> If so then traverse left or right (respectively)

        # else this is the lowest common ancestor and we can return it
        