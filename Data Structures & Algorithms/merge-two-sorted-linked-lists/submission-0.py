# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # We start the pointers at the head of the two linked lists
        # Compare the two curr nodes, if curr_1 < curr_2 then 

        prev = None
        head = None

        while list1 and list2:

            if list1.val <= list2.val:
                node = list1 # Store the node we want to become the new prev
                list1 = list1.next
            
            else:
                node = list2
                list2 = list2.next
            
            if prev is None:
                prev = node
                head = prev # Store the head of the pointer which we'll return later
            
            else:
                prev.next = node
                prev = prev.next

        if not list1: # If list1 is empty at the end then append the rest of list2 --> Be careful with none pointers
            if prev:
                prev.next = list2
            else:
                head = list2

        if not list2: # Likewise
            if prev:
                prev.next = list1
            else:
                head = list1
        
        return head
        