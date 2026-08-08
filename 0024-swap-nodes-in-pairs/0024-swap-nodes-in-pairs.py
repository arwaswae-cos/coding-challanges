# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        while curr != None and curr.next!= None:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        return head
