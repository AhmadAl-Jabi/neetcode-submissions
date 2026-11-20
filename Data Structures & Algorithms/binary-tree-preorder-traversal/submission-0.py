# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder is basically exploring the current node, then go left then go right
        # can do this recursively
        # base cases are when we hit a null node just return
        # can maintain an output array of integers (just append current value)

        output_arr = []

        def dfs(node):
            if not node:
                return
            
            output_arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return output_arr
        