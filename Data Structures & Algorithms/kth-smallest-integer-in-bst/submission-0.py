# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        # Brute forcy approach
        # can traverse entire tree to create arr of values (List[int])
        # then we sort the arr increasing order
        # and return the (n-1)th item from that 

# REDO BUT USE NONLOCAL VAR TRACKING THE VALUE OR SMT. Nested func is more intuitive
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth_value = -1
        self.count = 0

        def dfs(node,k):
            # so all we're returning is the count of what node we're at
            if not node:
                return 

            dfs(node.left,k)
            self.count += 1

            if self.count == k:
                self.kth_value = node.val

            dfs(node.right,k) # We don't care about storing anything from him
            # don't increase count again

            return 
        
        dfs(root,k)
        return self.kth_value


        # More optimal:
        # Visit the left most node first
        # from there we keep a count of nodes visited (including left most)
        # then we can visit its parent and its sibling
        # keep going until k hits the count in which we reutrn node.val
        

    
        