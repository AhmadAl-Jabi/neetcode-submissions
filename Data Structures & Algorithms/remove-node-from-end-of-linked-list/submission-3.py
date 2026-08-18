# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Easy approach that is O(2n) --> O(n) is two pass, first to count
        # Second to go behind the node we want to remove and set its .next to
        # .next.next and then remove the node.next of nth node
        # it works but let's try more optimal

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        # [1,2] n=2 --> [2]
        dummy = ListNode()
        dummy.next = head
        left_p, right_p = 0, 0 # keep track of distance
        left_n = right_n = dummy # the nodes themselves
        
        # Better approach is two pointers that maintain gap of n
        # march the right until we have that gap of n

        while right_n and right_n.next: # go until right_n at the end
            if right_p - left_p == n:
                left_p += 1
                left_n = left_n.next
            
            right_n = right_n.next
            right_p += 1
        
        # To avoid treating ends differently we can use dummy head
        # [dummy, 1, 2] n = 2 --> gap defined as right - left (keep track of these)
        # store left.next as remove_node
        # then we can set left.next = remove_node.next
        remove_node = left_n.next
        left_n.next = remove_node.next
        remove_node.next = None
        # remove_node.next = None
        
        return dummy.next if dummy.next != remove_node else left_n.next


        