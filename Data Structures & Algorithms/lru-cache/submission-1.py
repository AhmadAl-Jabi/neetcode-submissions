class ListNode:
    def __init__(self,val=0,key=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key= key


class LRUCache:
    # Our dict can be key value pairs of key being the int ID and value being the node object
    # Each node has value, prev and next (no need for key since that's stored in dict as key)

    # LRUCache(2), put[1,10], put[2,30], put[3, 20]
    # for [1,10] a node should be created since it's not in dict yet
    # we enter it to dict as dict[1] = Node(10) (next and prev are default None)

    # dummy_head <--> node_1 <-->  dummy_tail (in the case where count was 0 and we add a node)
    # dummy_head <--> node_1 <--> node_2 <-->  dummy_tail (after we just care about dummy_tail and its prev)
    # however both cases work the same since we're using dummy nodes 

    def __init__(self, capacity: int):
        # should hold counter of nodes (curr amount)
        self.curr_amount = 0
        # should hold capacity to compare curr_count to
        self.capacity = capacity

        # should hold a dict
        self.node_mapping = {}
        # should hold a dummy head 
        # should hold a dummy tail
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()

        # set dummy head next to tail
        # set dummy tail prev to head
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
    
    def move_to_back(self,curr_node):

        # detach it first
        if curr_node.prev and curr_node.next: #--> This checks that it was actually in list
            prev_node = curr_node.prev 
            next_node = curr_node.next
            prev_node.next = next_node
            next_node.prev = prev_node

        # then attach to end
        prev_node = self.dummy_tail.prev
        prev_node.next = curr_node
        curr_node.prev = prev_node
        curr_node.next = self.dummy_tail
        self.dummy_tail.prev = curr_node
        

    def get(self, key: int) -> int:
        # first check that it exists in dict --> if not return -1
        if key not in self.node_mapping:
            return -1 

        curr_node = self.node_mapping[key]

        # then check if dummy_tail.prev == curr_node --> if so skip & return curr_node.val
        if self.dummy_tail.prev != curr_node:
            self.move_to_back(curr_node)

        return curr_node.val
        

    def put(self, key: int, value: int) -> None:
        # If key exists:
        if key in self.node_mapping:
            # edit the node's val to the updated one
            node = self.node_mapping[key]
            node.val = value
            self.move_to_back(node)
            return
        
        curr_node = ListNode(value,key)

        # Else check first if we hit capacity --> If so we need to get rid of the oldest item
        if self.curr_amount == self.capacity:
            oldest_node = self.dummy_head.next
            self.dummy_head.next = oldest_node.next
            oldest_node.next.prev = self.dummy_head

            oldest_node.next = None
            oldest_node.prev = None

            #delete the key value pair from dict
            self.node_mapping.pop(oldest_node.key, None)
            self.curr_amount -= 1

        # then regardless we add node to the end of cache 
        self.move_to_back(curr_node)
        self.node_mapping[key] = curr_node
        self.curr_amount += 1

        

        
