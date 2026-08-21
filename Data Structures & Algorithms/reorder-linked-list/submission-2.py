# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        original = head


        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # So now slow is mid

        prev = None
        new_head = slow.next

        while new_head:
            next_node = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = next_node
        slow.next = None
        last_node = prev
        mid = prev
        segment = prev.next
        first_node = head
        third = segment

        while third:
            second = first_node.next
            third = segment.next
            first_node.next = segment
            segment.next = second

            first_node = second
            segment = third

        return original

'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) Find mid (use fast=head to get the usual mid behavior)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half starting at slow.next
        second = slow.next
        slow.next = None  # IMPORTANT: split the list

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3) Merge: first half = head, second half = prev
        first, second = head, prev
        while second:
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2
        # No return needed; list modified in place
            






        
        