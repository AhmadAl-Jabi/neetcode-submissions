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
        # Tricky part is lowkey the random thing since we need a proper way of making the nodes while keeping in mind it won't be in order
        if not head:
            return None

        # We'll actually need to make node = Node(val,next,random) calls
        # can maybe store the nodes and their deep copies first in a dict?
        # what info can we give the copies from the getgo?
            # can give its val
            # can't give its next and random unless we do one full pass first
        
        # Two pass approach:
        # First pass: create dict of original: deepcopy (with val and null refs)
        # Second pass: assign the randoms and next based on the key value pairs
        node_map = {}
        first_pointer = second_pointer = head

        while first_pointer:
            node_map[first_pointer] = Node(first_pointer.val) # other fields empty
            first_pointer = first_pointer.next
        
        while second_pointer:
            deep_copy = node_map[second_pointer]
            # should find the key value pair we want and extract the original "next" and original "random" as reference nodes 
            original_next = second_pointer.next
            original_random = second_pointer.random

            # then take new_next and new_random as the values of the keys
            new_next = node_map[original_next] if original_next else None
            new_random = node_map[original_random] if original_random else None

            deep_copy.next = new_next
            deep_copy.random = new_random

            second_pointer = second_pointer.next
        
        # return the value from key value pair of head
        return node_map[head]
        






        