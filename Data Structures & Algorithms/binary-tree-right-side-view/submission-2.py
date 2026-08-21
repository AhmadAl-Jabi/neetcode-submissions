# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Need a breadth first approach where at each level we take the node
        # furthest to the right

        # Start with queue 1 and basically add all its children to queue 2
        # Then we take the rightmost value in the queue1 to be our next node
        # Then we make queue 1 equal queue 2 and queue 2 empty again

        final_arr = []
        queue1 = []
        queue2 = []


        if root:
            queue1.append(root)

        while len(queue1) > 0:
            final_arr.append(queue1[-1].val)

            for node in queue1:

                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            queue1 = queue2
            queue2 = []       

        return final_arr
        