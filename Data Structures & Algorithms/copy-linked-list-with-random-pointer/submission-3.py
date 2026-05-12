# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}

        curr = head
        while curr:
            new = Node(curr.val)
            old_to_new[curr] = new
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]
        
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head:
#             return None
        
#         # Map original nodes to their copies
#         old_to_new = {}
        
#         # First pass: Create all nodes
#         curr = head
#         while curr:
#             old_to_new[curr] = Node(curr.val)
#             curr = curr.next
        
#         # Second pass: Set next and random pointers
#         curr = head
#         while curr:
#             if curr.next:
#                 old_to_new[curr].next = old_to_new[curr.next]
#             if curr.random:
#                 old_to_new[curr].random = old_to_new[curr.random]
#             curr = curr.next
        
#         return old_to_new[head]