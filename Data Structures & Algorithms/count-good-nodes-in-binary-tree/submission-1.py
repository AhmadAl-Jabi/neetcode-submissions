# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # I'm thinking we can have a nonlocal count of good nodes
        self.count = 0
        # we're just incrementing a count basically (start it at 1)
        # set the curr_max as root's val
        def searchGoodNodes(node, max_value):            
            # nested func just takes a node and the max value (which is highest val seen until now)
            # if not node return
            if not node:
                return

            # compare current node val to max --> if more then max_value becomes curr.val AND we do self.count += 1
            if node.val >= max_value:
                max_value = node.val
                self.count += 1

            # then either way we do nestedfunc on left and right
            # finally just return nothing
            searchGoodNodes(node.left,max_value)
            searchGoodNodes(node.right,max_value)

        # we basically we call nested func it with root and the max value (which initially is just root.val)
        searchGoodNodes(root,root.val)
        # return self.count
        return self.count


        