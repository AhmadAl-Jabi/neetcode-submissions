# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        self.is_subtree = False

        # Approach
        # Have subfunction that checks isSameTree of two nodes
        # returns either True or False
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2: #if one reached end but not other
                return False

            if node1.val != node2.val:
                return False

            left_tree = isSameTree(node1.left,node2.left)
            right_tree = isSameTree(node1.right,node2.right)

            return left_tree and right_tree

        # from isSubtree we call that func with current root and subRoot
        same_tree = isSameTree(root,subRoot)
        if same_tree:
            return True
        
        # At this point if root is null then subRoot CANT be null (otherwise same_tree would be True)
        left_search = self.isSubtree(root.left, subRoot) if root else False
        right_search = self.isSubtree(root.right, subRoot) if root else False
        
        return left_search or right_search




        