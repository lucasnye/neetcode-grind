# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head.next:
        #     return None
        # N = 0
        # curr = head
        # while curr:
        #     N += 1
        #     curr = curr.next
        
        # curr = head
        # prev = None
        # if N - n == 0:
        #     head = curr.next
        # else:
        #     for _ in range(N - n):
        #         prev = curr
        #         curr = curr.next
        #     prev.next = curr.next
        # return head
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next