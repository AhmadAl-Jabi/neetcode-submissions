# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we can do bfs with a deque and append the levels to a output_arr
        output_arr = []

        # deque = root
        queue = deque([root])

        # while deque:
        while queue:
            # sub_arr = []
            # for node in deque:
            sub_arr = []
            for i in range(len(queue)):
                # deque.popleft()
                node = queue.popleft()
                # if node:
                if node:
                    # deque.append(node.left)
                    # deque.append(node.right)
                    queue.append(node.left)
                    queue.append(node.right)
                    sub_arr.append(node.val)

            # output_arr.append(sub_arr)
            output_arr.append(sub_arr) if sub_arr else None
                
        # return output_arr
        return output_arr
        