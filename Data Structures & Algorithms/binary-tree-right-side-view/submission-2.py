# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1
        #2. 3
        #4
        # Only values of nodes that show up --> NO None
        # tree CAN be empty

        if not root:
            return []

        # queue = deque([root]) --> have the root for now
        queue = deque([root])
        # output_arr = []
        output_arr = []

        # Right side view is at any level of the tree what would be the rightmost node --> this translates to what is deque(-1)

        # while queue:
        while queue:
            # right_most = deque(-1)
            # output_arr.append(right_most) --> we have to make sure that we don't append None 
            n = 0
            right_most = queue[-1]
            output_arr.append(right_most.val)

            # for i in range(len(queue)):
            for i in range(len(queue)):
                # curr_node = deque.popleft()
                curr_node = queue.popleft()
                # add the children of any NON NULL nodes --> curr_node not none
                if curr_node:
                    queue.append(curr_node.left) if curr_node.left else None
                    queue.append(curr_node.right) if curr_node.right else None

        # return output_arr
        return output_arr





