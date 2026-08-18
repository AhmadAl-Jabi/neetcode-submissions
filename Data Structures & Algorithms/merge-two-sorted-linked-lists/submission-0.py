# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # So the way to merge is set the next of one guy to the other node
        # but we need a way to maintain the older heads when segmented (can store in a var)
        # [1,10,11], [2,3,5,7]
        if not list1:
            return list2
        
        if not list2:
            return list1

        if list1.val < list2.val:
            head = curr = list1
            list1 = list1.next
        
        else:
            head = curr = list2
            list2 = list2.next

        while list1 and list2:

            # if list 1 smaller make curr point at that, advance list 1
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            # else make curr point at list 2 and advance list 2
            else:
                curr.next = list2
                list2 = list2.next

            # advance curr regardless
            curr = curr.next

        # one list will end before the other, so make curr.next whatever is left
        curr.next = list1 or list2    
        return head

        