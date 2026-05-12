# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get slow and fast pointers and traverse such that slow pointer points to the middle
        # Reverse second half of linked list
        # Two pointer with first and second half
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        prev = None

        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        
        second_half = prev
        slow.next = None
        first_half = head
        
        while second_half:
            next_node_1 = first_half.next
            next_node_2 = second_half.next
            first_half.next = second_half
            second_half.next = next_node_1
            first_half = next_node_1
            second_half = next_node_2