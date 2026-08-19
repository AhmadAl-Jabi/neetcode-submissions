# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # can keep a carry that gets moved
        # l1 and l2 might not be same length
        # [9,9,9,9,9]
        # [9,9,9]

        # head = curr = ListNode()
        head = curr = ListNode()

        # carry = 0
        carry = 0
        # while l1 and l2:
        while l1 or l2:
            # total = l1.val + l2.val + carry
            # curr_val = total % 10
            # carry = total // 10 
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            curr_val = total % 10
            carry = total // 10

            # curr.val = curr_val
            curr.val = curr_val

            if (l1 and l1.next) or (l2 and l2.next):
                # curr.next = ListNode()
                curr.next = ListNode()
                # curr = curr.next
                curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # if carry --> Add one last node
        if carry:
           curr.next = ListNode(1)
           curr = curr.next

        return head

        
        