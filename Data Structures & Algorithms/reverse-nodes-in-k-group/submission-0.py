# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # I think we'll need some sort of "left" and "right" pointers where left is right before the k group and right is immediately after the k group --> might use a stack to keep track but maybe won't need it
        # all we're doing is reversing a linked list for each k group. We reverse each k linked list (can define as helper func)
        # maintain a count/dist between left and right (want count = k)

        # 1 -> 2 -> 3 -> 4   k = 2
        # prev = None, curr = 1 --> this would cause issues cuz 1 points at None even though it should point at 3 from get go
        # instead we just need to make sure we pass "3" as prev in the func call (the last node's next) --> 
        # we need to not only update the current list we're reversing, but also the immediate prev of the list (its next)
        # 2 -> 1 -> 4 -> 3
        first_reversal = True
        final_head = None
        counter = 0
        tail = head
        last_touched = None
   
        def reverseList(head, prev=None):
            nonlocal first_reversal, final_head

            if not head:
                return head

            # prev is last node we reversed (head of reversed part)
            # cur is the node we're processing (first unreversed node)
            # 1 -> 2 -> 3 -> 4 -> 5
            #None/prev 1h -> 2 -> ...
            prev, cur = prev, head

            for i in range(k):
                next_cur = cur.next
                cur.next = prev
                prev = cur
                cur = next_cur
            
            if first_reversal:
                final_head = prev
                first_reversal = not first_reversal

            return prev, head
        

        # can have a tail and counter that helps us figure out when to call reverseList
        while tail:
            tail = tail.next
            counter += 1

            if counter == k:
                n_head, n_prev = reverseList(head, tail)
                if last_touched:
                    last_touched.next = n_head
                last_touched = n_prev
                head = last_touched.next
                counter = 0
        
        return final_head 


