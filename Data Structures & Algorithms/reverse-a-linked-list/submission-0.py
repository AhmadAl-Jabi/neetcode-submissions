# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        point_to = None
        prev = None

        while head:
            prev = head.next
            head.next = point_to
            point_to = head
            head = prev

        return point_to
        