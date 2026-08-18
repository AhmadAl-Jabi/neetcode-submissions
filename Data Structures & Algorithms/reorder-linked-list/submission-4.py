# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # can have fast and slow to find the middle (I think it works)
        slow = prev_slow = fast = head
        if not head or not head.next:
            return

        # basically if fast is None or fast.next is None then slow should be at the middle (the first is if it's even and second if odd but doesn't matter)
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        mid_head = slow
        prev_slow.next = None

        # then the first half of the linked list is fine
        # but for the second half we can basically just reverse the linked list (which was a problem we did before)
        next_node, temp_node = None, None
        while mid_head:
            temp_node = mid_head.next
            mid_head.next = next_node
            next_node = mid_head
            mid_head = temp_node
        
        mid_head = next_node # this is the head of the reordered half
        
        # now all we need to do is have dummy point at first half nodes and second half in a staggered order (with first half first)
        #[1,2,3,4,5] --> [1,5,2,4,3]
        #[1,2,5,4,3] after reorder
        #[1,2,3,4]
        #[1,2,4,3]

        while head and mid_head:
            # we need to store what head and mid_head were pointing at

            head_history = head.next
            mid_head_history = mid_head.next

            # make head point at mid_head
            head.next = mid_head
            # make mid_head point at what head WAS pointing at
            mid_head.next = head_history if head_history else mid_head_history

            #head = what it was pointing at
            head = head_history
            #mid_head = what it was pointing at
            mid_head = mid_head_history