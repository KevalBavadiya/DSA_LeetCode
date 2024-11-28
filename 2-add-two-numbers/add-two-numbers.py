# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry, l1.val = divmod(l1.val + l2.val, 10)
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            carry, l1.val = divmod(l1.val+l2.val+carry, 10)
        
        if l2.next:
            l1.next = l2.next

        while l1.next:
            l1 = l1.next
            carry, l1.val = divmod(l1.val+carry, 10)

        if carry :
            l1.next = ListNode(carry)
        return head 

        