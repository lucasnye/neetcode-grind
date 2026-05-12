# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        curr = head
        prev = None
        if N - n == 0:
            head = curr.next
        else:
            for _ in range(N - n):
                prev = curr
                curr = curr.next
            prev.next = curr.next
        return head