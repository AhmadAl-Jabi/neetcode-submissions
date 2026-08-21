"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #Approach:
        #First pass to create a dict where keys are the random that the node points to and values are an array that initially just host the og nodes that I pass thru
        #Each time I go to a node, create a deep copy that has the same value and has a None next and random

        #Then when we created the dict that has the number keys and two nodes in each entry
        #We do another pass where we enumerate the dicts items (so each entry is indexed AND has the number, which tells you which random it should have)
        #Set the nodes next to be the next one in the enumerate, and make the random to be the node in key index
        #remember to access the vales[1] so we get the deep copy and not the og

        node_dict = {}
        curr_node = head
        #count = 0

        if not head:
            return head

        while curr_node:
          
            deep_copy = Node(curr_node.val, None, None)
            node_dict[curr_node] = deep_copy
            curr_node = curr_node.next
        
        dict_items = list(node_dict.items())
        for idx, item in enumerate(dict_items):
            #idx tells us the index of the current node
            #item gives us the key value pair as a tuple, so item[1][1] will access the deep copy in node_arr and item[0] gives rand val

            og_node = item[0]
            deep_node = item[1]
            deep_rand = node_dict[og_node.random] if og_node.random else None

            if idx < len(dict_items) - 1:
                deep_node.next = dict_items[idx + 1][1]
            
            else:
                deep_node.next = None
            
            if deep_rand:
                deep_node.random = deep_rand
            
            else:
                deep_node.random = None
        
        return node_dict[head]
            

        



        