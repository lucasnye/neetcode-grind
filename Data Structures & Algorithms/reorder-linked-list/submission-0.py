# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        prev = None

        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        second_half = prev
        
        first_half = head
        while second_half:
            first_next = first_half.next
            second_next = second_half.next
            first_half.next = second_half
            second_half.next = first_next
            first_half = first_next
            second_half = second_next
