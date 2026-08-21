# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nodes_seen = set()

        while head:
            if head not in nodes_seen:
                nodes_seen.add(head)
                head = head.next
            
            elif head in nodes_seen:
                return True

        return False
        