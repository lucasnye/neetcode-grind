# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (one list is exhausted)
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         p1, p2 = list1, list2
#         while p1 and p2:
#             if p1.val <= p2.val:
#                 next_node_2 = p2.next
#                 next_node_1 = p1.next
#                 p1.next = p2
#                 p2.next = next_node_1
#                 p2 = next_node_2
#             elif p1.val > p2.val:
#                 next_node_1 = p1.next
#                 next_node_2 = p2.next
#                 p1.next = p2
#                 p2
#         while p1:
#             pass
#         while p2:
#             pass