# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while (curr!=None):
            l += 1
            curr = curr.next
        if l==1 and n==1:
            return None
        elif l==n:
            return head.next
        elif l==2:
            if n==1:
                head.next = None
                return head
        curr = head
        for i in range(1,l-n):
            curr = curr.next
        curr.next = curr.next.next
        return head
        