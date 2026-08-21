# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # I think we need breadth first here. Start from top and make an array and add shit from that level
        # When we move to the next level, we make a new array and append items within that level
        # Rinse and repeat

        # One thing to be aware of is that we might have to think of levels a little diff, as in to get everyone in a level
        # we would need to go to the parent and append its kids, and to get to the next level we'd have to go back up and then back right
        # I don't think we need recursion here tbh. I think we can do a queue approach with levels

        final_arr = []
        first_queue = [root]
        second_queue = []


        # I'm thinking of doing two queues. First and second queue
        # Basically start with the root in first queue. Add first queue's values to final. Iterate 
        # Add the children to second queue. Add him to final_arr
        # First queue = second queue and second queue = [] once iteration is over

        # WE STORE VALUES NOT NODES
        if not root:
            return final_arr

        while len(first_queue) > 0:
            append_list = []
            for node in first_queue:
                append_list.append(node.val)
                
                if node.left:
                    second_queue.append(node.left)

                if node.right:
                    second_queue.append(node.right) 
            
            final_arr.append(append_list)
            first_queue = second_queue
            second_queue = []
        
        return final_arr




        

        
        