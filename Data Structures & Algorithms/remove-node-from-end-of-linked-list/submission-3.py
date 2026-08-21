# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #if n brings us to first then make head = head.next and return that
        #if n brings us to the very last guy then the second last guy points to null
        
        #otherwise we just go right before the node and set the .next to .next.next
        #and can set the .next guy's next to null
        
        count_node = curr_node = head
        count = 0

        while count_node:
            count += 1
            count_node = count_node.next
        
        if count - n == 0:
            head = head.next

        elif n == 1:
            # while and make the second last point null
            while curr_node.next.next:
                curr_node = curr_node.next
            
            curr_node.next = None
            
        else:
            new_count = 1

            while new_count < count - n:

                curr_node = curr_node.next
                new_count += 1
            
            temp = curr_node.next
            curr_node.next = curr_node.next.next
            temp.next = None

        return head


        