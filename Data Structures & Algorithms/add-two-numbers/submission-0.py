# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = l1
        head2 = l2

        num1 = ""
        num2 = ""

        while head1:
            num1 = str(head1.val) + num1
            head1 = head1.next
        
        while head2:
            num2 = str(head2.val) + num2
            head2 = head2.next
        
        total = str(int(num1) + int(num2))[::-1]

        t_head = ListNode(total[0],None)
        curr_node = t_head
        for char in total[1:]:
            curr_node.next = ListNode(char,None)
            curr_node = curr_node.next
        
        return t_head




        
        