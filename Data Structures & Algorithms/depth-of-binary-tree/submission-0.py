# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for depth we can definitely just use dfs and recursion

        # need a base case of if not root return --> return none since null node
        if not root:
            return 0
        
        # run maxDepth of its left
        left_depth = self.maxDepth(root.left)

        # run maxDepth of its right
        right_depth = self.maxDepth(root.right)

        # take depth of both and add one (including current)
        return max(left_depth, right_depth) + 1

        