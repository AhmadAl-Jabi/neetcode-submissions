# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can do this through dfs and basically build up an array of all the node values --> return the kth value in the end
        # recursively works here 
        node_values = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            node_values.append(node.val)
            dfs(node.right)
        dfs(root)
        return node_values[k-1]









