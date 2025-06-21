# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head, Rhead):
        ans = ListNode()
        k = ans
        while head and Rhead:
            if head.val < Rhead.val:
                k.next=head
                head = head.next
            else:
                k.next = Rhead
                Rhead = Rhead.next
            k = k.next
        k.next = head or Rhead
        return ans.next

    def findmid(self, head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None 
        return slow
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        mid = self.findmid(head)
        return self.merge(self.sortList(head), self.sortList(mid))